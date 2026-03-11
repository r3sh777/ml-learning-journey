import numpy as np

# ============================================
# DAY 1 — NumPy Basics
# What is NumPy? A supercharged Python list
# that can do math on entire arrays at once!
# ============================================

# --- Creating Arrays ---
prices = np.array([10, 20, 30, 40, 50])
print("Original prices:", prices)

# --- Vectorization: math on entire array at once (no loops needed!) ---
discounted = prices * 0.9          # 10% discount on all prices
new_prices = prices + 5            # add $5 to all prices
print("Discounted prices:", discounted)
print("New prices:", new_prices)

# --- Useful NumPy functions ---
scores = np.array([85, 92, 78, 95, 60, 88])
print("\nScores:", scores)
print("Average:", np.mean(scores))  # mean = average
print("Highest:", np.max(scores))   # maximum value
print("Lowest: ", np.min(scores))   # minimum value
print("Total:  ", np.sum(scores))   # sum of all values

# --- Boolean Masks: filter data without loops ---
average = np.mean(scores)
above_average = scores > average            # creates True/False array
print("\nAbove average?", above_average)
print("Scores above average:", scores[above_average])  # filter using mask
