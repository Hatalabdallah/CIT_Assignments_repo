# # Pandas Quiz

# ## Question 1

# What is the result of the following code?

# ```python
import pandas as pd
import numpy as np
import requests as rs
import random


# df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
# df.apply(lambda x: x.max() - x.min())
# print(df)

# A. col1    1.0
#     col2    1.0
#     col3    1.0
#     dtype: float64

# B. col1    1.0
#     col2    1.0
#     col3    1.0
#     dtype: float64

# C. col1    1.0
#     col2    1.0
#     col3    1.0
#     dtype: float64

# D. col1    1.0
#     col2    1.0
#     col3    1.0
#     dtype: float64

# ## Question 2

# Download a csv file from https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip and load it into a pandas dataframe. How many rows and columns are there?

# def download_csv(url):
#     r = rs.get(url) 
#     with open('data2.csv', 'wb') as f: 
#         f.write(r.content) 
    
# import os 

# if not os.path.exists('data2.csv'): 
#     download_csv('https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip') 

# df = pd.read_csv('data2.csv') 
# print(df)


# ## Question 3

# What method can be used to get the number of non-NA values in a pandas dataframe?

A

# A. `df.count()`

# B. `df.na_count()`

# C. `df.na_values()`

# D. `df.na_count()`

# ## Question 4

# Create a dataframe with 10 rows and 3 columns, 
# where the values are random numbers between 1 and 10 (inclusive). 
# Then, replace all values greater than 5 with the value 10.

# arr = [random.randint(1, 10) for i in range(1, 10)]

# df = pd.DataFrame(arr)
# print(df)

# ## Question 5
# create a dataframe from this link https://jsonplaceholder.typicode.com/albums

import json

albums = rs.get('https://jsonplaceholder.typicode.com/albums').json()
df = pd.DataFrame(albums)

print(df.head())