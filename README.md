import math

"""
Calculates the straight-line Euclidean distance between two points 
using the distance formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
"""

print("Enter the coordinates for two points:")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute squared differences and final distance
x_diff_sq = math.pow(x2 - x1, 2)
y_diff_sq = math.pow(y2 - y1, 2)
distance = math.sqrt(x_diff_sq + y_diff_sq)

print(f"\nDistance between ({x1}, {y1}) and ({x2}, {y2}): {distance:.2f}")

# ==========================================
# REFLECTION AND EVALUATION
# ==========================================
# Using the math library is much more practical than writing all calculations from scratch 
# because it saves development time and utilizes pre-tested, highly optimized functions. 
# In this activity, relying on math.sqrt() and math.pow() allowed me to implement the Euclidean 
# distance formula instantly without needing to manually write complex square root approximation algorithms.
