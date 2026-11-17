# Titanic Exploratory Data Analysis (EDA)

## Project Overview
This project performs Exploratory Data Analysis on the Titanic passenger dataset using Python. The goal is to understand passenger information, identify patterns, and explore factors associated with survival.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset
- Dataset: Titanic
- Total Records: 891 passengers
- Original Columns: 12
- Cleaned Columns: 11

## Project Tasks
1. Load and inspect the Titanic dataset.
2. Identify missing values and duplicate records.
3. Clean the dataset by handling missing values.
4. Analyze survival rates by gender and passenger class.
5. Explore passenger age and fare information.
6. Generate visualizations.
7. Create a final EDA report.

## Key Findings
- Total passengers analyzed: 891
- Survivors: 342
- Non-survivors: 549
- Overall survival rate: 38.38%
- Female survival rate: 74.20%
- Male survival rate: 18.89%
- First-class survival rate: 62.96%
- Second-class survival rate: 47.28%
- Third-class survival rate: 24.24%

## Visualizations
The project generates four charts:
- Survival Count
- Survival by Gender
- Survival by Passenger Class
- Age Distribution

## Project Files
- `titanic.csv` – Original dataset
- `cleaned_titanic.csv` – Cleaned dataset
- `eda_analysis.py` – Initial data exploration
- `clean_data.py` – Data cleaning
- `survival_analysis.py` – Survival analysis
- `visualize_eda.py` – Data visualization
- `eda_report.py` – Final EDA report
- `requirements.txt` – Python dependencies

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis scripts:

```bash
python eda_analysis.py
python clean_data.py
python survival_analysis.py
python visualize_eda.py
python eda_report.py
```

## Conclusion
This project demonstrates how Python can be used to inspect, clean, analyze, and visualize data. The analysis shows differences in survival rates across passenger genders and classes.

---
**Project:** CodeAlpha Data Analytics Internship – Task 2: Exploratory Data Analysis