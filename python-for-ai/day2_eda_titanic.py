import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Shape:", df.shape)                  

print("\nColumns:", df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())                   

print("\nStatistical summary:")
print(df.describe())

print("\nSurvival counts:")
print(df["Survived"].value_counts())     

female_survived = df[(df["Sex"] == "female") & (df["Survived"] == 1)].shape[0]
male_survived   = df[(df["Sex"] == "male")   & (df["Survived"] == 1)].shape[0]
print("\nFemale survivors:", female_survived)  
print("Male survivors:  ", male_survived)       

df["Survived"].value_counts().plot(kind="bar", color=["red", "green"])
plt.title("Titanic Survival Count")
plt.xlabel("0 = Died, 1 = Survived")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()