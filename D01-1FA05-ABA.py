import math

# Ask the user for coordinates of the two points
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute the distance using math.pow() and math.sqrt()
delta_x = math.pow(x2 - x1, 2)
delta_y = math.pow(y2 - y1, 2)
distance = math.sqrt(delta_x + delta_y)

# Display the result clearly, formatted to two decimal places
print(f"\nThe distance between the two points is: {distance:.2f}")

# ==========================================
# REFLECTION AND EVALUATION
# ==========================================
# Using the math library is much more practical than writing all calculations from scratch 
# because it saves development time and utilizes pre-tested, highly optimized functions. 
# In this activity, relying on math.sqrt() and math.pow() allowed me to implement the Euclidean 
# distance formula instantly without needing to manually write complex square root approximation algorithms.
