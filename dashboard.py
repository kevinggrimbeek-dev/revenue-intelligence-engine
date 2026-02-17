import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Revenue Intelligence Dashboard", layout="wide")

# -----------------------------
# Synthetic Data Generator
# -----------------------------

np.random.seed(42)

def generate_sample_data(num_accounts=200):
    df = pd.DataFrame({
        "company": [f"Company_{i}" for i in range(num_accounts)],
        "monthly_revenue": np.random.randint(500, 10000, num_accounts),
        "engagement_score": np.random.randint(10, 100, num_accounts),
        "support_tickets": np.random.poisson(4, num_accounts),
        "days_to_renewal": np.random.randint(0, 180, num_accounts),
        "contract_status": np.random.choice(
            ["Active", "Active", "Active", "Expired"],
            num_accounts
        )
    })

    df["prev_engagement_score"] = (
        df["engagement_score"] + np.random.randint(-20, 20, num_accounts)
    ).clip(0, 100)

    return df

# -----------------------------
# Risk Logic
# -----------------------------

def analyze_revenue_health(df):

    # Engagement trend
    df["engagement_change"] = df["engagement_score"] - df["prev_engagement_score"]

    def classify_trend(x):
        if x < -15:
            return "Sharp Decline"
        elif x < 0:
            return "Declining"
        elif x > 15:
            return "Strong Growth"
        elif x > 0:
            return "Improving"
        else:
            return "Stable"

    df["trend_status"] = df["engagement_change"].apply(classify_trend)

    # Churn probability model
    df["churn_probability"] = (
        (100 - df["engagement_score"]) * 0.4 +
        df["support_tickets"] * 5 +
        (180 - df["days_to_renewal"]) * 0.1
    ) / 100

    df["churn_probability"] = df["churn_probability"].clip(0, 1)

    # Revenue at risk
    df["revenue_at_risk"] = df["monthly_revenue"] * df["churn_probability"]

    # Health tier
    def assign_health(prob):
        if prob >= 0.75:
            return "At Risk"
        elif prob >= 0.5:
            return "Watchlist"
        else:
            return "Healthy"

    df["health_tier"] = df["churn_probability"].apply(assign_health)

    return df

# -----------------------------
# App UI
# -----------------------------

st.title("📊 Revenue Intelligence Dashboard")

df = generate_sample_data()
df = analyze_revenue_health(df)

# KPIs
total_revenue = df["monthly_revenue"].sum()
revenue_at_risk = df["revenue_at_risk"].sum()
percent_risk = (revenue_at_risk / total_revenue) * 100

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Revenue At Risk", f"${revenue_at_risk:,.0f}")
col3.metric("% Revenue At Risk", f"{percent_risk:.2f}%")

st.divider()

# Filter
selected_tier = st.selectbox(
    "Filter by Health Tier",
    ["All", "Healthy", "Watchlist", "At Risk"]
)

if selected_tier != "All":
    df = df[df["health_tier"] == selected_tier]

# Table
st.subheader("Account Overview")
st.dataframe(df.sort_values("revenue_at_risk", ascending=False))

# Revenue at Risk Chart
st.subheader("Revenue at Risk Distribution")
risk_summary = df.groupby("health_tier")["revenue_at_risk"].sum()
st.bar_chart(risk_summary)