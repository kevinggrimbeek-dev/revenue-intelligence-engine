# Revenue Intelligence Engine

## Overview

The Revenue Intelligence Engine is a Python-based Revenue Operations system designed to detect revenue instability before churn occurs.

Rather than focusing only on revenue growth, this project models revenue risk using weighted scoring, probabilistic churn estimation, and engagement trend detection.

The system simulates a SaaS customer base and demonstrates how RevOps can proactively identify high-risk accounts, quantify revenue exposure, and prioritize intervention.

---

## Core Capabilities

- Revenue Health Index (Weighted Scoring Model)
- Churn Probability Estimation
- Month-over-Month Engagement Trend Detection
- Revenue-at-Risk Forecasting
- Intervention Flagging
- Executive Revenue Summary Output
- Visual Revenue Distribution Dashboard (Streamlit)

---

## Revenue Health Index Components

The model evaluates accounts using:

- Engagement Score
- Support Ticket Volume
- Days to Renewal
- Contract Status
- Month-over-Month Engagement Change

Each account is categorized into:

- Healthy
- Watchlist
- At Risk

---

## System Architecture

The project consists of two main components:

### 1. Revenue Intelligence Engine (`revenue_intelligence_engine.py`)
- Generates simulated SaaS account data
- Calculates churn probability
- Computes revenue at risk
- Assigns health tiers
- Produces executive revenue summaries
- Exports a structured CSV report

### 2. Revenue Dashboard (`dashboard.py`)
- Interactive Streamlit dashboard
- Health tier filtering
- Revenue-at-risk visualization
- Account-level risk inspection
- Executive-level KPI display

---

## Executive Outputs

The engine produces:

- Total Revenue
- Total Revenue at Risk
- Percentage Revenue at Risk
- Top 10 High-Risk Accounts
- Revenue-at-Risk by Health Tier Visualization
- Exportable Revenue Risk Report (CSV)

---

## Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Streamlit

---

## Installation (VS Code)

1. Open the project folder in VS Code.
2. Open the integrated terminal.
3. Install dependencies:

pip install -r requirements.txt

---

## Running the Revenue Engine

To generate the revenue report and executive summary:

python revenue_intelligence_engine.py

This will:
- Print executive metrics to the terminal
- Generate revenue visualizations
- Export `revenue_risk_report.csv`

---

## Running the Dashboard

To launch the interactive dashboard:

streamlit run dashboard.py

Then open your browser at:

http://localhost:8501

---

## Business Impact

This project demonstrates how Revenue Operations can:

- Quantify hidden revenue risk
- Detect churn signals before contract expiration
- Prioritize intervention using data
- Move from reactive churn analysis to proactive revenue protection

---

## Author

Built by Kevin Grimbeek

Revenue Operations professional with 8+ years in sales and performance strategy, specializing in revenue intelligence, churn risk modeling, and proactive account health systems.

Open to Revenue Operations, RevOps Analytics, and Revenue Strategy opportunities.
