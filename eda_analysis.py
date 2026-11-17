
import pandas as pd

# Load Titanic dataset
df = pd.read_csv("titanic.csv")

# 1. Display first 5 records
print("\n========== FIRST 5 RECORDS ==========")
print(df.head())

# 2. Display dataset shape
print("\n========== DATASET SHAPE ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 3. Display column names
print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

# 4. Display data types
print("\n========== DATA TYPES ==========")
print(df.dtypes)

# 5. Dataset information
print("\n========== DATASET INFORMATION ==========")
df.info()

# 6. Statistical summary
print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# 7. Check missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 8. Check duplicate records
print("\n========== DUPLICATE RECORDS ==========")
print(df.duplicated().sum())

print("\nEDA exploration completed successfully!")
