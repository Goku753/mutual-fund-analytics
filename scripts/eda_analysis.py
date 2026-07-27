import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# Create visualization folder
# ----------------------------------------------------
os.makedirs("visualizations", exist_ok=True)

# ----------------------------------------------------
# Connect Database
# ----------------------------------------------------
conn = sqlite3.connect("database/mutual_fund.db")

# ----------------------------------------------------
# Load Tables
# ----------------------------------------------------
fund_df = pd.read_sql('SELECT * FROM "01_fund_master"', conn)

nav_df = pd.read_sql('SELECT * FROM "02_nav_history"', conn)

aum_df = pd.read_sql('SELECT * FROM "03_aum_by_fund_house"', conn)

txn_df = pd.read_sql('SELECT * FROM "08_investor_transactions"', conn)

portfolio_df = pd.read_sql('SELECT * FROM "09_portfolio_holdings"', conn)

performance_df = pd.read_sql('SELECT * FROM "07_scheme_performance"', conn)

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\nFund Master Shape:", fund_df.shape)

# ====================================================
# 1. Fund Category Distribution
# ====================================================

plt.figure(figsize=(10,6))

fund_df["category"].value_counts().plot(kind="bar")

plt.title("Fund Category Distribution")
plt.xlabel("Category")
plt.ylabel("Number of Schemes")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("visualizations/category_distribution.png")
plt.close()

# ====================================================
# 2. Top 10 Fund Houses
# ====================================================

plt.figure(figsize=(12,6))

fund_df["fund_house"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Fund Houses")
plt.xlabel("Fund House")
plt.ylabel("Number of Schemes")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("visualizations/top_fund_houses.png")
plt.close()

# ====================================================
# 3. Risk Category Distribution
# ====================================================

plt.figure(figsize=(8,8))

fund_df["risk_category"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Risk Category Distribution")

plt.tight_layout()
plt.savefig("visualizations/risk_distribution.png")
plt.close()

# ====================================================
# 4. Expense Ratio Distribution
# ====================================================

plt.figure(figsize=(10,6))

fund_df["expense_ratio_pct"].hist(bins=20)

plt.title("Expense Ratio Distribution")
plt.xlabel("Expense Ratio (%)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("visualizations/expense_ratio_distribution.png")
plt.close()

# ====================================================
# 5. Top Fund Houses by AUM
# ====================================================

top_aum = (
    aum_df
    .groupby("fund_house")["aum_crore"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

top_aum.plot(kind="bar")

plt.title("Top Fund Houses by AUM")
plt.xlabel("Fund House")
plt.ylabel("AUM (Crore)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("visualizations/aum_distribution.png")
plt.close()

# ====================================================
# 6. Transaction Type
# ====================================================

plt.figure(figsize=(8,6))

txn_df["transaction_type"].value_counts().plot(kind="bar")

plt.title("Transaction Type Distribution")

plt.tight_layout()
plt.savefig("visualizations/transaction_type.png")
plt.close()

# ====================================================
# 7. Payment Mode
# ====================================================

plt.figure(figsize=(8,6))

txn_df["payment_mode"].value_counts().plot(kind="bar")

plt.title("Payment Mode Distribution")

plt.tight_layout()
plt.savefig("visualizations/payment_mode.png")
plt.close()

# ====================================================
# 8. Top Investor States
# ====================================================

plt.figure(figsize=(12,6))

txn_df["state"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Investor States")

plt.tight_layout()
plt.savefig("visualizations/state_distribution.png")
plt.close()

# ====================================================
# 9. Sector Distribution
# ====================================================

sector = (
    portfolio_df
    .groupby("sector")["weight_pct"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

sector.plot(kind="bar")

plt.title("Top Portfolio Sectors")
plt.xlabel("Sector")
plt.ylabel("Weight (%)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("visualizations/sector_distribution.png")
plt.close()

# ====================================================
# 10. NAV Trend
# ====================================================

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values("date")

daily_nav = (
    nav_df
    .groupby("date")["nav"]
    .mean()
)

plt.figure(figsize=(15,6))

plt.plot(
    daily_nav.index,
    daily_nav.values
)

plt.title("Average Daily NAV Trend")
plt.xlabel("Date")
plt.ylabel("Average NAV")

plt.tight_layout()
plt.savefig("visualizations/nav_trend.png")
plt.close()

# ====================================================
# 11. Top Rated Schemes
# ====================================================

top_rating = (
    performance_df
    .groupby("scheme_name")["morningstar_rating"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

top_rating.plot(kind="bar")

plt.title("Top Rated Mutual Fund Schemes")

plt.tight_layout()
plt.savefig("visualizations/top_rated_schemes.png")
plt.close()

conn.close()

print("\nAll visualizations created successfully.")
print("Saved inside the visualizations folder.")