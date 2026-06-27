import os
import pandas as pd

# -----------------------------------
# Create output folder automatically
# -----------------------------------
os.makedirs("../output", exist_ok=True)

# -----------------------------------
# Load cleaned dataset
# -----------------------------------
df = pd.read_csv("../dataset/complaints_cleaned.csv")

# -----------------------------------
# Convert Date received to datetime
# -----------------------------------
df["Date received"] = pd.to_datetime(df["Date received"])

# Create Month column
df["Month"] = df["Date received"].dt.to_period("M")

# ===================================
# Product Analysis
# ===================================
product_analysis = (
    df["Product"]
    .value_counts()
    .reset_index()
)

product_analysis.columns = ["Product", "Complaint Count"]

# ===================================
# Company Analysis
# ===================================
company_analysis = (
    df["Company"]
    .value_counts()
    .reset_index()
)

company_analysis.columns = ["Company", "Complaint Count"]

# ===================================
# State Analysis
# ===================================
state_analysis = (
    df["State"]
    .value_counts()
    .reset_index()
)

state_analysis.columns = ["State", "Complaint Count"]

# ===================================
# Submission Channel Analysis
# ===================================
channel_analysis = (
    df["Submitted via"]
    .value_counts()
    .reset_index()
)

channel_analysis.columns = ["Submission Channel", "Complaint Count"]

# ===================================
# Monthly Trend
# ===================================
monthly_analysis = (
    df.groupby("Month")
    .size()
    .reset_index(name="Complaint Count")
)

# ===================================
# Save all analysis
# ===================================
product_analysis.to_csv("../output/product_analysis.csv", index=False)

company_analysis.to_csv("../output/company_analysis.csv", index=False)

state_analysis.to_csv("../output/state_analysis.csv", index=False)

channel_analysis.to_csv("../output/channel_analysis.csv", index=False)

monthly_analysis.to_csv("../output/monthly_analysis.csv", index=False)

print("===================================")
print("Analysis Completed Successfully!")
print("===================================")

print("\nFiles Created:")
print("- product_analysis.csv")
print("- company_analysis.csv")
print("- state_analysis.csv")
print("- channel_analysis.csv")
print("- monthly_analysis.csv")