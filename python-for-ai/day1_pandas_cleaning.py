import pandas as pd

data = {
    "name": ["Ravi", "Sara", "John"],
    "age":  [25, 30, 22],
    "city": ["Chennai", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)
print("Our DataFrame:")
print(df)

print("\nShape (rows, columns):", df.shape)
print("\nSelect one column:")
print(df["city"])

print("\nPeople older than 24:")
print(df[df["age"] > 24])

messy_data = {
    "name":  ["Alice", "Bob", None, "Diana", "Eve"],  
    "score": [85, None, 72, 300, 90],                 
    "grade": ["A", "b", "C", "a", "B"]               
}
df_messy = pd.DataFrame(messy_data)
print("\nMessy data:")
print(df_messy)

print("\nMissing values per column:")
print(df_messy.isnull().sum())

df_clean = df_messy.dropna(subset=["name"])

df_clean["score"] = df_clean["score"].fillna(df_clean["score"].mean())

df_clean = df_clean[df_clean["score"] <= 100]

df_clean["grade"] = df_clean["grade"].str.upper()

print("\nCleaned data:")
print(df_clean)
