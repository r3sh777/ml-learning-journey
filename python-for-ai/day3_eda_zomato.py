import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\there\Documents\PythonProjects\Datasets\Zomatodataset\zomato.csv", encoding="latin-1")

# Chart 1: Online delivery vs rating
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Has Online delivery",
            y="Aggregate rating", palette="coolwarm")
plt.title("Does Online Delivery Affect Restaurant Ratings?")
plt.xlabel("Has Online Delivery")
plt.ylabel("Average Rating")
plt.show()

# Chart 2: Price range vs rating
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Price range",
            y="Aggregate rating", palette="Blues")
plt.title("Do Expensive Restaurants Rate Higher?")
plt.xlabel("Price Range (1=Cheap, 4=Expensive)")
plt.ylabel("Average Rating")
plt.show()