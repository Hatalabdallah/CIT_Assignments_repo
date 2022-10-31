# # Numpy Array Quiz

# ## Question 1

# What is the result of the following code?

# ```python
import numpy as np
import statistics as st
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)
# answer is [5 7 9]


# ## Question 2

# Create a numpy array of 10 zeros. and reshape it to (2, 5)

arr = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
arr = arr.reshape(2, 5)
print(arr)


# ## Question 3

# Find Mean, Mode, Median, Standard Deviation of the following data

# ```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

data = np.array(data)

mean = data.mean()

median = np.median(data)

mode = st.mode(data)

standard_deviation = np.std(data)
print(f'Mean: {mean}, Mode: {mode}, Median: {median} and Standard Deviation: {standard_deviation}')

# ```

# ## Question 4

# create a 6x6 numpy array with random values and find the min and max values

x = np.random.random((6,6))

print("Original Array:")

print(x) 

xmin, xmax = x.min(), x.max()

print("Minimum and Maximum Values:")

print(xmin, xmax)


# ## Question 5

# create a 3D numpy array and reshape it to 2D

arr = np.array([[[ 1 , 2],[ 3 , 4],[ 5 , 6]],[[ 7 , 8],[ 9 ,10],[11 ,12]]]) # 3D array
arr = arr.reshape(2, 6)
print(arr) # 2D array

# ## Question 6

# create 1D array from this data

# ```python
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)
print(data.reshape(9, ))
# ```