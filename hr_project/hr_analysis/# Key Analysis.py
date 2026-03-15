# Key Analysis


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

#  Load the cleaned data
df = pd.read_csv(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\hr_cleaned.csv')
print("✅ Cleaned data loaded!")
print("Shape:", df.shape)



# ANALYSIS 1: Attrition Rate by Department


dept_attrition = df.groupby('Department')['Attrition_Num'].mean() * 100
dept_attrition = dept_attrition.sort_values(ascending=False)

print("\n📊 Attrition Rate by Department:")
print(dept_attrition)

plt.figure(figsize=(7, 4))
dept_attrition.plot(kind='bar', color=['#E74C3C', '#E67E22', '#3498DB'], edgecolor='white')
plt.title('Attrition Rate by Department (%)')
plt.ylabel('Attrition Rate (%)')
plt.xlabel('Department')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\dept_attrition.png', dpi=150)
plt.show()
print("✅ Chart 1 saved!")



# ANALYSIS 2: Overtime Impact on Attrition


overtime_attrition = df.groupby('OverTime')['Attrition_Num'].mean() * 100

print("\n📊 Attrition Rate by Overtime:")
print(overtime_attrition)

plt.figure(figsize=(5, 4))
overtime_attrition.plot(kind='bar', color=['#2ECC71', '#E74C3C'], edgecolor='white')
plt.title('Attrition Rate: Overtime vs No Overtime (%)')
plt.ylabel('Attrition Rate (%)')
plt.xlabel('Works Overtime?')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\overtime_attrition.png', dpi=150)
plt.show()
print("✅ Chart 2 saved!")



# ANALYSIS 3: Salary vs Attrition


print("\n📊 Average Monthly Income:")
print(df.groupby('Attrition')['MonthlyIncome'].mean().round(0))

plt.figure(figsize=(7, 4))
sns.boxplot(data=df, x='Attrition', y='MonthlyIncome',
            palette={'No': '#3498DB', 'Yes': '#E74C3C'})
plt.title('Monthly Income: Stayed vs Left')
plt.xlabel('Attrition')
plt.ylabel('Monthly Income (USD)')
plt.tight_layout()
plt.savefig(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\salary_attrition.png', dpi=150)
plt.show()
print("✅ Chart 3 saved!")



# ANALYSIS 4: Job Satisfaction vs Attrition


satisfaction_attrition = df.groupby('JobSatisfaction')['Attrition_Num'].mean() * 100

print("\n📊 Attrition Rate by Job Satisfaction Level:")
print(satisfaction_attrition)

plt.figure(figsize=(6, 4))
satisfaction_attrition.plot(kind='bar',
                             color=['#E74C3C', '#E67E22', '#3498DB', '#2ECC71'],
                             edgecolor='white')
plt.title('Attrition Rate by Job Satisfaction Level')
plt.ylabel('Attrition Rate (%)')
plt.xlabel('Job Satisfaction (1=Low → 4=Very High)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\satisfaction_attrition.png', dpi=150)
plt.show()
print("✅ Chart 4 saved!")


print("\n🎉 All 4 analyses complete! Charts saved to hr_cleaned folder.")