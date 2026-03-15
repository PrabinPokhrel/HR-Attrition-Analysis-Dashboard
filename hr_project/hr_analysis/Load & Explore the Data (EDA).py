# STEP 2: Load & Explore the Data (EDA)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set_theme(style="whitegrid")

# 2.1 Load the data 
df = pd.read_csv(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\data\WA_Fn-UseC_-HR-Employee-Attrition.csv')

print("✅ Data loaded successfully!")
print("Rows & Columns:", df.shape)

# 2.2 First look 
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values (should all be 0):")
print(df.isnull().sum())

# 2.3 Drop useless columns 
# These 3 columns have the same value for every row — not useful
df.drop(columns=['EmployeeCount', 'StandardHours', 'Over18'], inplace=True)
print("\n✅ Useless columns dropped.")
print("New shape:", df.shape)   # Should be (1470, 32)

# 2.4 Convert Attrition text → number 
# Yes → 1,  No → 0
# Needed for charts and ML model later
df['Attrition_Num'] = df['Attrition'].map({'Yes': 1, 'No': 0})
print("\n✅ Attrition column converted to numbers.")

#  2.5 Overall attrition rate 
rate = df['Attrition_Num'].mean() * 100
print(f"\n📊 Overall Attrition Rate: {rate:.1f}%")

#  2.6 Summary statistics 
print("\nSummary Statistics:")
print(df.describe())

#  2.7 Plot: Attrition distribution 
plt.figure(figsize=(6, 4))
df['Attrition'].value_counts().plot(
    kind='bar',
    color=['steelblue', 'salmon'],
    edgecolor='white'
)
plt.title('Employee Attrition: Stayed vs Left')
plt.xlabel('Attrition')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\attrition_distribution.png', dpi=150)
plt.show()
print("✅ Chart saved!")

# 2.8 Save cleaned data 
df.to_csv(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\hr_cleaned.csv', index=False)
print("\n✅ Cleaned data saved to hr_cleaned folder!")