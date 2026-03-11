import numpy as np

prices = np.array([10, 20, 30, 40, 50])
print("Original prices:", prices)

discounted = prices * 0.9          
new_prices = prices + 5           
print("Discounted prices:", discounted)
print("New prices:", new_prices)

scores = np.array([85, 92, 78, 95, 60, 88])
print("\nScores:", scores)
print("Average:", np.mean(scores))  
print("Highest:", np.max(scores))  
print("Lowest: ", np.min(scores))  
print("Total:  ", np.sum(scores))   


average = np.mean(scores)
above_average = scores > average            
print("\nAbove average?", above_average)
print("Scores above average:", scores[above_average])  
