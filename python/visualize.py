import os
import pandas as pd
import matplotlib.pyplot as plt

# Create charts folder
os.makedirs("../output/charts", exist_ok=True)

# Load data
product_df = pd.read_csv("../output/product_analysis.csv")

# Take Top 10
top10 = product_df.head(10)

# Create figure
plt.figure(figsize=(12,6))

bars = plt.barh(
    top10["Product"],
    top10["Complaint Count"]
)

plt.title("Top 10 Products with Most Complaints", fontsize=16)
plt.xlabel("Complaint Count")
plt.ylabel("Product")

# Largest on top
plt.gca().invert_yaxis()

# Add values on bars
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 50,
        bar.get_y() + bar.get_height()/2,
        f"{int(width):,}",
        va="center"
    )

plt.tight_layout()

plt.savefig("../output/charts/01_top_products.png", dpi=300)

plt.close()
# ======================================
# Top 10 Companies
# ======================================

company_df = pd.read_csv("../output/company_analysis.csv")

top10_company = company_df.head(10)

plt.figure(figsize=(12,6))

bars = plt.barh(
    top10_company["Company"],
    top10_company["Complaint Count"]
)

plt.title("Top 10 Companies with Most Complaints", fontsize=16)
plt.xlabel("Complaint Count")
plt.ylabel("Company")

plt.gca().invert_yaxis()

for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 20,
        bar.get_y() + bar.get_height()/2,
        f"{int(width):,}",
        va="center"
    )

plt.tight_layout()

plt.savefig("../output/charts/02_top_companies.png", dpi=300)

plt.close()

state_df = pd.read_csv("../output/state_analysis.csv")

top10_state = state_df.head(10)

plt.figure(figsize=(10,6))

bars = plt.barh(
    top10_state["State"],
    top10_state["Complaint Count"]
)

plt.title("Top 10 States with Most Complaints")
plt.xlabel("Complaint Count")

plt.gca().invert_yaxis()

for bar in bars:
    width = bar.get_width()
    plt.text(width + 20,
             bar.get_y() + bar.get_height()/2,
             str(int(width)),
             va="center")

plt.tight_layout()

plt.savefig("../output/charts/03_top_states.png", dpi=300)

plt.close()
channel_df = pd.read_csv("../output/channel_analysis.csv")

plt.figure(figsize=(7,7))

plt.pie(
    channel_df["Complaint Count"],
    labels=channel_df["Submission Channel"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Complaint Submission Channels")

plt.savefig("../output/charts/04_submission_channels.png", dpi=300)

plt.close()
monthly_df = pd.read_csv("../output/monthly_analysis.csv")

plt.figure(figsize=(12,6))

plt.plot(
    monthly_df["Month"],
    monthly_df["Complaint Count"],
    marker="o"
)

plt.title("Monthly Complaint Trend")
plt.xlabel("Month")
plt.ylabel("Complaint Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../output/charts/05_monthly_trend.png", dpi=300)

plt.close()

print("✅ All charts generated successfully!")