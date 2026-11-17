
import pandas as pd

df = pd.read_csv("cleaned_titanic.csv")

total = len(df)
survivors = df["Survived"].sum()
deaths = total - survivors

survival_rate = df["Survived"].mean() * 100

gender_rate = (
    df.groupby("Sex")["Survived"].mean() * 100
)

class_rate = (
    df.groupby("Pclass")["Survived"].mean() * 100
)

print("=" * 50)
print("       TITANIC EXPLORATORY DATA ANALYSIS")
print("=" * 50)

print("\n1. DATASET OVERVIEW")
print("Total Passengers:", total)
print("Total Columns:", len(df.columns))

print("\n2. SURVIVAL SUMMARY")
print("Survivors:", survivors)
print("Non-survivors:", deaths)
print("Survival Rate:", round(survival_rate, 2), "%")

print("\n3. GENDER INSIGHTS")
print(gender_rate.round(2))

print("\n4. PASSENGER CLASS INSIGHTS")
print(class_rate.round(2))

print("\n5. AGE INSIGHTS")
print("Average Age:", round(df["Age"].mean(), 2))
print("Average Survivor Age:",
      round(df[df["Survived"] == 1]["Age"].mean(), 2))

print("\n6. FARE INSIGHTS")
print("Average Fare:", round(df["Fare"].mean(), 2))
print("Average Survivor Fare:",
      round(df[df["Survived"] == 1]["Fare"].mean(), 2))

print("\n7. KEY FINDINGS")
print("- Female passengers had a higher survival rate.")
print("- First-class passengers had the highest survival rate.")
print("- Overall survival rate was approximately 38.38%.")

print("\nEDA REPORT GENERATED SUCCESSFULLY!")
