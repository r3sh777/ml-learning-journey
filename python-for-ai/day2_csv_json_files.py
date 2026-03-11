import pandas as pd

data = {
    "name":  ["Ravi", "Sara", "John"],
    "score": [85, 92, 78],
    "city":  ["Chennai", "Mumbai", "Delhi"]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

#Save as CSV
df.to_csv("students.csv", index=False)     
print("\nSaved as students.csv")

#Save as JSON
df.to_json("students.json", orient="records", indent=2)
print("Saved as students.json")

#Read CSV back 
df_from_csv = pd.read_csv("students.csv")
print("\nRead back from CSV:")
print(df_from_csv)

#Read JSON back 
df_from_json = pd.read_json("students.json")
print("\nRead back from JSON:")
print(df_from_json)

#Convert CSV to JSON
df_convert = pd.read_csv("students.csv")
df_convert.to_json("students_converted.json", orient="records", indent=2)
print("\nConverted CSV → JSON")
