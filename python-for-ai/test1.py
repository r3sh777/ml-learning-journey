import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\there\Documents\PythonProjects\Datasets\StudentPerformanceFactors.csv")

# Relationship between Hours Studied and Exam Score
sns.scatterplot(data=df, x="Hours_Studied", y="Exam_Score", alpha=0.4)

plt.title("Hours Studied vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.show()

