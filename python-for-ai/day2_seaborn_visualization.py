import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ============================================
# DAY 2 — Seaborn Visualization
# Seaborn = beautiful charts with less code!
# Used on the Student Performance dataset.
# ============================================

# --- Load dataset (update path if needed) ---
df = pd.read_csv(r"C:\Users\there\Documents\PythonProjects\Datasets\StudentPerformanceFactors.csv")

# Remove impossible score (over 100)
df = df[df["Exam_Score"] <= 100]

# --- Chart 1: Histogram — distribution of exam scores ---
# Shows: most students score between 65-70 (bell curve shape)
sns.histplot(data=df, x="Exam_Score", bins=20, color="steelblue")
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# --- Chart 2: Barplot — does motivation level affect scores? ---
# Shows: barely any difference between High/Medium/Low motivation!
sns.barplot(data=df, x="Motivation_Level", y="Exam_Score", palette="coolwarm")
plt.title("Exam Score by Motivation Level")
plt.xlabel("Motivation Level")
plt.ylabel("Average Exam Score")
plt.tight_layout()
plt.show()

# --- Chart 3: Scatterplot — hours studied vs exam score ---
# Shows: more study hours = higher scores (clear upward trend!)
sns.scatterplot(data=df, x="Hours_Studied", y="Exam_Score", alpha=0.4)
plt.title("Hours Studied vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.show()

# --- Chart 4: Heatmap — correlations between all numeric columns ---
# Shows: Hours_Studied has highest correlation with Exam_Score
numeric_df  = df.select_dtypes(include="number")  # numbers only
correlation = numeric_df.corr()                    # correlation matrix
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap — Student Performance")
plt.tight_layout()
plt.show()
