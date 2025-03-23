# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball

np_baseball=np.array(baseball)


# Print out type of np_baseball
print(type(np_baseball))

# problem 4

print(np.array([True, 1, 2]) + np.array([3, 4, False]))
# it can also be written as the followinf
print(np.array([4, 3, 0]) + np.array([0, 2, 2]))

# problem 3 import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110

print(np_height_in[100:111])