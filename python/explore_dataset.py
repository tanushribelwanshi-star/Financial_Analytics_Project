import pandas as pd

# Load the sample dataset
df = pd.read_csv("../dataset/complaints_sample.csv")

print("First 5 rows:")
print(df.head())

print("\n------------------------")

print("Column Names:")
print(df.columns)

print("\n------------------------")

print("Dataset Shape:")
print(df.shape)

print("\n------------------------")

print("Data Types:")
print(df.dtypes)

print("\n------------------------")

print("Dataset Information:")
print(df.info())