import numpy as np

# Range of threshold values
threshold_range = np.arange(0.5, 1.0, 0.1)

# Convert NumPy array to Python list
threshold_list = threshold_range.tolist()

print(threshold_list)
