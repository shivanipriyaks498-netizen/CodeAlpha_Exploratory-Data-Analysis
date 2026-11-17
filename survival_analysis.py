
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_titanic.csv")

print("========== TITANIC SURVIVAL ANALYSIS ==========")

# Total survival count
print("\n1. SURVIVAL COUNT")
print(df["Survived"].value_counts())

survival_rate = df["Survived"].mean() * 100

print("\nOverall Survival Rate:", round(survival_rate, 2), "%")

# Survival by gender
print("\n2. SURVIVAL BY GENDER")
gender_survival = df.groupby("Sex")["Survived"].mean() * 100
print(gender_survival.round(2))

# Survival by passenger class
print("\n3. SURVIVAL BY PASSENGER CLASS")
class_survival = df.groupby("Pclass")["Survived"].mean() * 100
print(class_survival.round(2))

# Average age of survivors
print("\n4. AVERAGE AGE OF SURVIVORS")
avg_age = df[df["Survived"] == 1]["Age"].mean()
print(round(avg_age, 2))

# Average fare of survivors
print("\n5. AVERAGE FARE OF SURVIVORS")
avg_fare = df[df["Survived"] == 1]["Fare"].mean()
print(round(avg_fare, 2))

print("\nSurvival analysis completed successfully!")
