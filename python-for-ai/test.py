import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Bar chart — how many survived vs died?
df["Survived"].value_counts().plot(kind="bar", color=["red", "green"])

print(df.describe())

female_survived = df[df["Sex"] == "female"][df["Survived"] == 1].shape[0]

male_survived = df[df["Sex"] == "male"][df["Survived"] == 1].shape[0]

print("Female survivors:", female_survived)
print("Male survivors:", male_survived)

plt.title("Titanic Survival Count")
plt.xlabel("0 = Died, 1 = Survived")
plt.ylabel("Number of Passengers")
plt.show()