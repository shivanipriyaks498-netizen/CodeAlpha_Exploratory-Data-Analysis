
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_titanic.csv")

sns.set_theme(style="whitegrid")

# 1. Survival Count
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Survived")
plt.title("Titanic Passenger Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.savefig("survival_count.png")
plt.close()

# 2. Survival by Gender
plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="Sex", y="Survived")
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.savefig("survival_by_gender.png")
plt.close()

# 3. Survival by Passenger Class
plt.figure(figsize=(7, 5))
sns.barplot(data=df, x="Pclass", y="Survived")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.savefig("survival_by_class.png")
plt.close()

# 4. Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", bins=30, kde=True)
plt.title("Titanic Passenger Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.savefig("age_distribution.png")
plt.close()

print("All EDA visualizations created successfully!")
print("Generated: 4 PNG chart files")
