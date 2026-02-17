import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================
# Revenue Intelligence Engine
# =====================================

np.random.seed(42)


# -----------------------------
# Synthetic Data Generator
# -----------------------------
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
        df["engagement_score"] +
        np.random.randint(-20, 20, num_accounts)
    ).clip(0, 100)

    return df


# -----------------------------
# Revenue Health Analysis
# -----------------------------
def analyze_revenue_health(df):

    # Engagement Trend
    df["engagement_change"] = (
        df["engagement_score"] -
        df["prev_engagement_score"]
    )

    def classify_trend(change):
        if change < -15:
            return "Sharp Decline"
        elif change < 0:
            return "Declining"
        elif change > 15:
            return "Strong Growth"
        elif change > 0:
            return "Improving"
        else:
            return "Stable"

    df["trend_status"] = df["engagement_change"].apply(classify_trend)

    # Churn Probability Model
    df["churn_probability"] = (
        (100 - df["engagement_score"]) * 0.4 +
        df["support_tickets"] * 5 +
        (180 - df["days_to_renewal"]) * 0.1
    ) / 100

    df["churn_probability"] = df["churn_probability"].clip(0, 1)

    # Revenue At Risk
    df["revenue_at_risk"] = (
        df["monthly_revenue"] *
        df["churn_probability"]
    )

    # Health Tier Classification
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
# Print Summary
# -----------------------------
def print_summary(df):

    total_revenue = df["monthly_revenue"].sum()
    revenue_at_risk = df["revenue_at_risk"].sum()
    percent_at_risk = (revenue_at_risk / total_revenue) * 100

    print("\n===== REVENUE HEALTH SUMMARY =====")
    print(f"Total Revenue: {total_revenue}")
    print(f"Revenue At Risk: {revenue_at_risk:.2f}")
    print(f"% Revenue At Risk: {percent_at_risk:.2f}%")

    print("\n===== TOP 10 HIGH RISK ACCOUNTS =====")
    print(
        df.sort_values("revenue_at_risk", ascending=False)
        .head(10)[
            [
                "company",
                "monthly_revenue",
                "health_tier",
                "churn_probability",
                "revenue_at_risk",
                "trend_status"
            ]
        ]
    )


# -----------------------------
# Generate Visuals
# -----------------------------
def generate_visuals(df):

    risk_summary = df.groupby("health_tier")["revenue_at_risk"].sum()

    plt.figure()
    risk_summary.plot(kind="bar")
    plt.title("Revenue At Risk by Health Tier")
    plt.ylabel("Revenue At Risk")
    plt.xlabel("Health Tier")
    plt.tight_layout()
    plt.show()


# -----------------------------
# Main Function
# -----------------------------
def main():

    df = generate_sample_data()
    final_df = analyze_revenue_health(df)

    print_summary(final_df)
    generate_visuals(final_df)

    # Export CSV
    final_df.to_csv("revenue_risk_report.csv", index=False)
    print("\nReport exported to revenue_risk_report.csv")


# -----------------------------
# Run Script
# -----------------------------
if __name__ == "__main__":
    main()