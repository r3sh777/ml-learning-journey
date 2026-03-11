import pandas as pd
import numpy as np

# ============================================
# DAY 1 — Pandas & Data Cleaning
# Pandas lets us work with tables (DataFrames)
# just like Excel, but in Python!
# ============================================

# --- Creating a DataFrame from scratch ---
data = {
    "name": ["Ravi", "Sara", "John"],
    "age":  [25, 30, 22],
    "city": ["Chennai", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)
print("Our DataFrame:")
print(df)

# --- Exploring a DataFrame ---
print("\nShape (rows, columns):", df.shape)
print("\nSelect one column:")
print(df["city"])

# --- Filtering rows with conditions ---
print("\nPeople older than 24:")
print(df[df["age"] > 24])

# ============================================
# DATA CLEANING — fixing messy real-world data
# ============================================

messy_data = {
    "name":  ["Alice", "Bob", None, "Diana", "Eve"],  # None = missing
    "score": [85, None, 72, 300, 90],                 # 300 = impossible score!
    "grade": ["A", "b", "C", "a", "B"]               # inconsistent capitals
}
df_messy = pd.DataFrame(messy_data)
print("\nMessy data:")
print(df_messy)

# --- Check missing values ---
print("\nMissing values per column:")
print(df_messy.isnull().sum())

# --- Fix 1: Drop rows where name is missing ---
df_clean = df_messy.dropna(subset=["name"])

# --- Fix 2: Fill missing score with average ---
df_clean["score"] = df_clean["score"].fillna(df_clean["score"].mean())

# --- Fix 3: Remove impossible scores ---
df_clean = df_clean[df_clean["score"] <= 100]

# --- Fix 4: Uppercase all grades ---
df_clean["grade"] = df_clean["grade"].str.upper()

print("\nCleaned data:")
print(df_clean)
