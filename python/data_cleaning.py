import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/complaints_sample.csv")

print("Original Shape:", df.shape)

# Remove rows where important columns are missing
df = df.dropna(subset=[
    "Product",
    "Issue",
    "Company",
    "Complaint ID"
])

# Convert dates into datetime format
df["Date received"] = pd.to_datetime(df["Date received"])
df["Date sent to company"] = pd.to_datetime(df["Date sent to company"])

print("Cleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv("../dataset/complaints_cleaned.csv", index=False)

print("Cleaned dataset saved successfully!")