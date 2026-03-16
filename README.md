# HR-Attrition-Analysis-Dashboard

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow?style=flat&logo=powerbi)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=flat&logo=scikit-learn)
![pandas](https://img.shields.io/badge/pandas-Data%20Analysis-green?style=flat&logo=pandas)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)

> A complete end-to-end HR Analytics project that analyses employee attrition, identifies key drivers, builds machine learning models to predict who will leave, and visualizes everything in an interactive Power BI dashboard.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Tools & Technologies](#-tools--technologies)
- [Analysis Steps](#-analysis-steps)
- [Key Findings](#-key-findings)
- [ML Model Results](#-ml-model-results)
- [Business Recommendations](#-business-recommendations)
- [Dashboard Preview](#-dashboard-preview)
- [How to Run](#-how-to-run)
- [Conclusion](#-conclusion)

---

## 📌 Project Overview

Employee attrition is one of the most costly challenges for any organization. Replacing a single employee can cost between **$10,000 – $50,000** in recruitment, onboarding, and lost productivity. This project uses data analytics and machine learning to:

- Understand **why** employees leave
- Identify **which departments** are at highest risk
- Predict **who** is likely to leave next
- Provide **actionable recommendations** to reduce turnover

---

## 💼 Business Problem

> *"Our company has a 16.1% attrition rate. We need to understand the root causes and predict which employees are at risk of leaving so HR can take proactive action."*

**Key Questions Answered:**
1. Which department has the highest attrition rate?
2. Does working overtime significantly increase the chance of leaving?
3. Is there a salary gap between employees who stayed vs left?
4. Does job satisfaction level predict attrition?
5. Can we build a model to predict who will leave?

---

## 📊 Dataset

| Property | Details |
|---|---|
| **Name** | IBM HR Analytics Employee Attrition Dataset |
| **Source** | [Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset) |
| **Rows** | 1,470 employees |
| **Columns** | 35 features |
| **Missing Values** | None |
| **Target Column** | `Attrition` (Yes / No) |

**Key Features Used:**
- `Department` — Sales, R&D, Human Resources
- `OverTime` — Yes / No
- `MonthlyIncome` — Employee salary
- `JobSatisfaction` — Scale 1 (Low) to 4 (Very High)
- `Age`, `TotalWorkingYears`, `YearsAtCompany`
- `WorkLifeBalance`, `JobRole`, `MaritalStatus`

---

## 📁 Project Structure
```
hr_project/
│
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv    ← raw dataset
│
├── hr_cleaned/
│   ├── hr_cleaned.csv                            ← cleaned data
│   ├── attrition_distribution.png                ← chart outputs
│   ├── dept_attrition.png
│   ├── overtime_attrition.png
│   ├── salary_attrition.png
│   ├── satisfaction_attrition.png
│   ├── model_comparison.png
│   ├── confusion_matrix.png
│   └── feature_importance.png
│
├── hr_analysis.py                                ← EDA & analysis code
├── hr_model.py                                   ← ML model code
├── HR_Attrition_Dashboard.pbix                   ← Power BI dashboard
└── README.md
```

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **Python 3.8+** | Data cleaning, analysis, ML models |
| **pandas** | Data manipulation and aggregation |
| **numpy** | Numerical operations |
| **matplotlib / seaborn** | Data visualization and charts |
| **scikit-learn** | Machine learning models |
| **Power BI Desktop** | Interactive dashboard |

---

## 🔄 Analysis Steps

### Step 1 — Data Loading & Cleaning
- Loaded 1,470 rows × 35 columns
- Dropped 3 useless columns: `EmployeeCount`, `StandardHours`, `Over18`
- Converted `Attrition` (Yes/No) to numeric (1/0) for analysis
- Confirmed zero missing values

### Step 2 — Exploratory Data Analysis (EDA)
- Calculated overall attrition rate: **16.1%**
- Explored distributions of age, salary, satisfaction scores
- Identified key patterns across departments and job roles

### Step 3 — Key Analysis (4 Business Questions)
- Attrition rate by department
- Overtime impact on attrition
- Salary comparison between who stayed vs left
- Job satisfaction levels vs attrition rate

### Step 4 — Machine Learning Models
- Encoded categorical columns using LabelEncoder
- Split data: 80% train / 20% test
- Trained Logistic Regression and Random Forest models
- Evaluated with accuracy score, classification report, confusion matrix
- Extracted feature importance from Random Forest

### Step 5 — Power BI Dashboard
- Imported hr_cleaned.csv into Power BI Desktop
- Created DAX measure for dynamic Attrition Rate calculation
- Built 6 visuals: KPI cards, bar charts, donut chart, slicer
- Applied consistent color theme (red = high risk, green = low risk)

### Step 6 — Insights & Recommendations
- Translated data findings into 12 concrete business actions
- Prioritized actions by impact and feasibility

---

## 🔍 Key Findings

### 1. 🏢 Attrition by Department
| Department | Attrition Rate |
|---|---|
| Sales | **20.6%** 🔴 Highest |
| Human Resources | **19.0%** 🟠 |
| Research & Development | **13.8%** 🟢 Lowest |

### 2. ⏰ Overtime Impact
| Overtime | Attrition Rate |
|---|---|
| Yes | **30.5%** 🔴 — 3x higher risk |
| No | **10.4%** 🟢 |

> Overtime is the single strongest predictor of attrition in this dataset.

### 3. 💰 Salary vs Attrition
| Group | Avg Monthly Income |
|---|---|
| Stayed | **$6,832** |
| Left | **$4,787** |
| Gap | **$2,045 per month** |

### 4. 😊 Job Satisfaction vs Attrition
| Satisfaction Level | Attrition Rate |
|---|---|
| Level 1 — Low | **22.0%** 🔴 |
| Level 2 — Medium | **17.0%** 🟠 |
| Level 3 — High | **14.0%** 🟢 |
| Level 4 — Very High | **15.0%** 🟢 |

---

## 🤖 ML Model Results

| Model | Accuracy |
|---|---|
| Logistic Regression | **88.1%** |
| Random Forest | **86.4%** |

### Top 10 Attrition Predictors (Random Forest)
1. 💰 MonthlyIncome
2. ⏰ OverTime
3. 🎂 Age
4. 📅 TotalWorkingYears
5. 🏢 YearsAtCompany
6. 👔 JobRole
7. 📊 JobLevel
8. 🔄 YearsInCurrentRole
9. 👨‍💼 YearsWithCurrManager
10. 😊 JobSatisfaction

---

## 💡 Business Recommendations

### Department Risk
- ✅ Conduct targeted exit interviews in the Sales department
- ✅ Review commission structures and workload in Sales
- ✅ Study R&D retention practices and replicate across departments

### Overtime
- ✅ Cap mandatory overtime at 10 hours per month per employee
- ✅ Hire contract staff during peak periods
- ✅ Introduce time-off compensation for overtime workers

### Salary
- ✅ Benchmark salaries against market rates for roles under $5,000 per month
- ✅ Implement structured pay raise schedules (5–8% every 2 years minimum)
- ✅ Prioritize salary reviews in Sales where both pay and attrition are problematic

### Job Satisfaction
- ✅ Run quarterly anonymous satisfaction surveys
- ✅ Flag teams scoring Level 1–2 for immediate manager check-ins
- ✅ Create clearer career development and promotion paths

---

## 📊 Dashboard Preview

Power BI Dashboard includes:
- **KPI Cards** — Total Employees, Attrition Rate, Avg Salary, Avg Age
- **Bar Chart** — Attrition Rate by Department
- **Bar Chart** — Overtime Impact on Attrition
- **Column Chart** — Average Salary: Stayed vs Left
- **Column Chart** — Attrition by Job Satisfaction Level
- **Donut Chart** — Overall Attrition Split
- **Slicer** — Filter entire dashboard by Department

*To view the dashboard, download HR_Attrition_Dashboard.pbix and open with Power BI Desktop (free).*

---

## ▶️ How to Run

### 1. Clone the repository
```
https://github.com/PrabinPokhrel/HR-Attrition-Analysis-Dashboard
```

### 2. Install required libraries
```
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 3. Download the dataset
- Go to https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
- Download WA_Fn-UseC_-HR-Employee-Attrition.csv
- Place it inside the data/ folder

### 4. Run the analysis
```
python hr_analysis.py
```

### 5. Run the ML models
```
python hr_model.py
```

### 6. View the dashboard
- Open HR_Attrition_Dashboard.pbix in Power BI Desktop

---

## ✅ Conclusion

This project successfully identified the key drivers of employee attrition:

- **Overtime** is the #1 risk factor — employees working overtime leave at 3x the rate
- **Sales department** has the highest attrition at 20.6%
- **Lower salary** strongly correlates with attrition — $2,045 per month gap between who stayed vs left
- **Low job satisfaction** doubles the risk of leaving
- The **Random Forest model** achieved 86% accuracy in predicting attrition

By acting on these findings, HR departments can significantly reduce turnover, save recruitment costs, and build a more stable and engaged workforce.

---

## 👤 Author

**PRABIN POKHREL**

**DALARNA UNIVERSITY**


---


*⭐ If you found this project helpful, please give it a star on GitHub!*
