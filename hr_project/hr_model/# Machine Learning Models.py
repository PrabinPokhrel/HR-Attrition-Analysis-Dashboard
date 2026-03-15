# Machine Learning Models


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                              confusion_matrix, ConfusionMatrixDisplay)

sns.set_theme(style="whitegrid")

# Load cleaned data 
df = pd.read_csv(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\hr_cleaned.csv')
print("✅ Data loaded!")
print("Shape:", df.shape)



# 4.1 Encode Text Columns → Numbers
# ML models only understand numbers, not words like "Yes/No"

le = LabelEncoder()

text_columns = ['Attrition', 'BusinessTravel', 'Department', 'EducationField',
                'Gender', 'JobRole', 'MaritalStatus', 'OverTime']

for col in text_columns:
    df[col] = le.fit_transform(df[col])

print("\n✅ Text columns converted to numbers!")
print(df[text_columns].head(3))



# 4.2 Define Features (X) and Target (y)
# X = columns we use to predict  →  all columns except Attrition
# y = what we predict            →  Attrition (0=Stayed, 1=Left)

X = df.drop(columns=['Attrition', 'Attrition_Num'])
y = df['Attrition']

print("\n✅ Features and Target defined!")
print("Features (X) shape:", X.shape)   # (1470, 30)
print("Target  (y) shape:", y.shape)    # (1470,)
print("\nTarget value counts:")
print(y.value_counts())                 # 0=Stayed: 1233,  1=Left: 237


# 4.3 Split Data into Train and Test Sets
# 80% for training  →  model learns from this
# 20% for testing   →  we check how accurate the model is

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n✅ Data split into Train and Test sets!")
print(f"Training set : {X_train.shape[0]} rows")   # 1176 rows
print(f"Testing set  : {X_test.shape[0]} rows")    # 294 rows



# MODEL 1: Logistic Regression
# Simple and fast — good for understanding direction of impact


print("\n⏳ Training Logistic Regression model...")
lr_model = LogisticRegression(max_iter=500, random_state=42)
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_pred) * 100
print(f"\n── Logistic Regression Results ──")
print(f"✅ Accuracy: {lr_accuracy:.1f}%")
print("\nDetailed Report:")
print(classification_report(y_test, lr_pred, target_names=['Stayed', 'Left']))


# MODEL 2: Random Forest
# More powerful — finds complex patterns in data


print("\n⏳ Training Random Forest model...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_pred) * 100
print(f"\n── Random Forest Results ──")
print(f"✅ Accuracy: {rf_accuracy:.1f}%")
print("\nDetailed Report:")
print(classification_report(y_test, rf_pred, target_names=['Stayed', 'Left']))


# 4.4 Model Comparison Chart


plt.figure(figsize=(5, 4))
models = ['Logistic Regression', 'Random Forest']
accuracies = [lr_accuracy, rf_accuracy]
colors = ['#3498DB', '#2ECC71']

plt.bar(models, accuracies, color=colors, edgecolor='white', width=0.5)
plt.title('Model Accuracy Comparison')
plt.ylabel('Accuracy (%)')
plt.ylim(80, 95)
for i, v in enumerate(accuracies):
    plt.text(i, v + 0.2, f'{v:.1f}%', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\model_comparison.png', dpi=150)
plt.show()
print("✅ Model comparison chart saved!")



# 4.5 Confusion Matrix — Random Forest
# Shows: how many predictions were correct vs wrong

cm = confusion_matrix(y_test, rf_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                               display_labels=['Stayed', 'Left'])
disp.plot(cmap='Blues')
plt.title('Random Forest — Confusion Matrix')
plt.tight_layout()
plt.savefig(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\confusion_matrix.png', dpi=150)
plt.show()
print("✅ Confusion matrix saved!")


# 4.6 Feature Importance
# Which factors matter MOST in predicting who will leave?

feature_importance = pd.Series(rf_model.feature_importances_,
                                index=X.columns)
top10 = feature_importance.sort_values(ascending=False).head(10)

print("\n📊 Top 10 Factors That Predict Attrition:")
print(top10)

plt.figure(figsize=(8, 5))
top10.sort_values().plot(kind='barh', color='steelblue', edgecolor='white')
plt.title('Top 10 Factors That Predict Attrition (Random Forest)')
plt.xlabel('Importance Score')
plt.tight_layout()
plt.savefig(r'C:\Users\WELCOME\Desktop\DataAnalysis_Projects\hr_project\hr_cleaned\feature_importance.png', dpi=150)
plt.show()
print("✅ Feature importance chart saved!")


print("\n🎉 Step 4 Complete! All ML results and charts saved.")
