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