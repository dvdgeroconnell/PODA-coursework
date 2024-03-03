# Week 5 - various functions associated with numpy
# Author: David O'Connell

import numpy as np
import matplotlib.pyplot as plt

rolls = np.random.randint(1, 7, 1000)
print(rolls[:25])
mean = np.mean(rolls)
print(mean)
std = np.std(rolls)
print(std)

# in the following code, 2 arrays are returned. The first goes into 
# unique_rolls, the second goes into roll_counts.
unique_rolls, roll_counts = np.unique(rolls, return_counts=True)
print(unique_rolls)
print(roll_counts)

plt.bar(unique_rolls, roll_counts)

# This function prints the bar chart in its own window.
plt.show()