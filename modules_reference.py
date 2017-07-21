'''
Python Modules Quick Reference

https://github.com/steincastillo/python-reference.git
Edited by: Stein Castillo
http://www.stein-castillo.com

Table of Contents:
    numpy
    pandas
'''

### NUMPY ###
import numpy as np  # standard module import

# Creating numpy arrays
a = np.array([2, 3, 4])                     # Creates a single numpy array. values must be passed as a list
b = np.array([1.2, 3.5, 5.1])           # Creates a numpy array
c = np.array([[1, 2, 3],  [4, 5,6]])    # Creates a 2 dimensional array
d = np.array([1, 2, 3], dtype = 'float64') # Creates numpy array indicating the data type

# Other methods to create numpy arrays
a0 = np.zeros((3,4))            # Creates an array of zeros with the specified shape
a1 = np.ones((3,4))             # Creates an array of ones with the specified shape
a0 = np.zeros((3,4), dtype = 'int16')          # Creates an array of zeros with the specified shape and data type
a0 = np.zeros((3,4), dtype = np.int16)      # Creates an array of zeros with the specified shape and data type
az = np.empty((3,4), dtype = np.int8)        # Creates unitialized array of specified shape and data type

# Basic arrays methods
a.dtype             # returns the array type: int32
b.dtype             # returns the array type: float64
d.dtype             # Returns float64
a.ndim              # Returns array dimensions: 1
c.ndim              # Retruns array dimensions: 2
a.shape            # Returns a tuple with the array shape: (3,)
c.shape            # Retruns a tuple with array shape: (2, 3)


### PANDAS ###
import pandas as pd         # Standard module import


# Reading datasets
dataframe = pd.read_csv(file)                                               # Imports a CSV file as dataframe
dataframe = pd.read_csv(file, delimiter=r"\s+")                   # Imports a <SPACE> separated file
dataframe = pd.read_csv(file, delim_whitespace=True)     # Imports a <SPACE> separated file
dataframe = pd.read_csv(file, header = None)                    # Imports a file that has no headers
dataframe = pd.read_csv(file, na_filter = False)                  # na_filter=False converts all nam into empty strings
dataframe.drop('feature', axis = 1)                                        # Eliminates a column 'feature' from the dataframe
dataframe = pd.read_csv(file).drop('feature', axis = 1)       # Reads the dataframe and eliminates the column feature

# Convert dataset into numpy array
dataset =  dataframe.values

# Describe the dataset (features, count, mean, std dev, min, etc)
dataframe.describe()
