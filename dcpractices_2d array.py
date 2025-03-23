import numpy as np
np_height = np.array([1.73,1.68,1.71,1.89,1.79])
np_weight = np.array([65.4,59.2,63.6,88.4,68.7])
type(np_height)
type(np_weight)
np_2d =np.array([[1.73,1.68,1.71,1.89,1.79],
                [65.4,59.2,63.6,88.4,68.7]])
print(np_2d)
print(np_2d.shape)

#Now lets try to find the elements from this matrix, there are two ways to to it

print(np_2d[0][2])
print(np_2d[0,2])

# It is way to print the entire row or selective columns
print(np_2d[:,1:3])
print(np_2d[1,:])

#Exercise 1

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

#Exercise 2

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

#Exercise 3

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49, :])
# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player

print(np_baseball[123,0])

#Exercise 4

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball+updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592,1])

# Print out product of np_baseball and conversion

print(np_baseball*conversion)

#Exercise 5

# Create np_height_in from np_baseball
np_height_in= np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

#Exercise 6

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))