import sqlite3
import pandas as pd

# Connect to SQLite database
connection = sqlite3.connect("../sql/complaints.db")

print("Database connected successfully!")

# Load cleaned dataset
df = pd.read_csv("../dataset/complaints_cleaned.csv")

# Store data into SQLite
df.to_sql(
    "complaints",
    connection,
    if_exists="replace",
    index=False
)

print("Data imported successfully!")

# Close connection
connection.close()

print("Database closed.")