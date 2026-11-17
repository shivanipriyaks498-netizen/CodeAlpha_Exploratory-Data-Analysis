
import pandas as pd

# Load original dataset
df = pd.read_csv("titanic.csv")

print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with mode
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)

# Drop Cabin column because it has too many missing values
df = df.drop(columns=["Cabin"])

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("cleaned_titanic.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset shape:", df.shape)
