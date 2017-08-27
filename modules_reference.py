'''
Python Modules Quick Reference

https://github.com/steincastillo/python-reference.git
Edited by: Stein Castillo
http://www.stein-castillo.com

Table of Contents:
    numpy
    scypi
    pandas
'''

### NUMPY ###
# Description: Provides advance functionality to operate and manipualte arrays

import numpy as np  # standard module import

# Creating numpy arrays
a = np.array([2, 3, 4])                 # Creates a single numpy array. values must be passed as a list
b = np.array([1.2, 3.5, 5.1])           # Creates a numpy array
c = np.array([[1, 2, 3],  [4, 5,6]])    # Creates a 2 dimensional array
d = np.array([1, 2, 3], dtype = 'float64') # Creates numpy array indicating the data type

# Other methods to create numpy arrays
a0 = np.zeros((3,4))            # Creates an array of zeros with the specified shape
a1 = np.ones((3,4))             # Creates an array of ones with the specified shape
a0 = np.zeros((3,4), dtype = 'int16')        # Creates an array of zeros with the specified shape and data type
a0 = np.zeros((3,4), dtype = np.int16)       # Creates an array of zeros with the specified shape and data type
az = np.empty((3,4), dtype = np.int8)        # Creates unitialized array of specified shape and data type
ar = np.arange(5)                            # Creates an 1 dimension array with the values in a rage: ar = [0, 1, 2, 3, 4]
ar = np.arange(5, dtype = np.int16)          # As above but set the data type to int16
ar = np.random.random(4)                     # Creates a 1 dimension array of 4 random values (between 0-1)
ar = np.random.random((3,2))                 # Creates a 2 dimension array of 3x2 random values (between 0-1)


# Numpy data types
ad = np.zeros ((3,4), dtype= np.int8)       # Byte (-128 to 127)
ad = np.zeros ((3,4), dtype= np.int16)     # Integer (-32768 to 32767)
ad = np.zeros ((3,4), dtype= np.int32)     # Integer ((-2147483648 to 2147483647)
ad = np.zeros ((3,4), dtype= np.int64)     # Integer (-9223372036854775808 to 9223372036854775807)
ad = np.zeros ((3,4), dtype= np.uint8)     # Unsigned intger (0 to 255)
ad = np.zeros ((3,4), dtype= np.uint16)     # Unsigned intger (0 to 65535)
ad = np.zeros ((3,4), dtype= np.uint32)     # Unsigned intger (0 to 4294967295)
ad = np.zeros ((3,4), dtype= np.uint64)     # Unsigned intger (0 to 18446744073709551615)
ad = np.zeros ((3,4), dtype= np.float_)       # Shorthand for float64
ad = np.zeros ((3,4), dtype= np.float16)     # Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
ad = np.zeros ((3,4), dtype= np.float32)     # Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
ad = np.zeros ((3,4), dtype= np.float64)     # Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
ad = np.zeros ((3,4), dtype= np.complex_)   # Shorthand for complex128
ad = np.zeros ((3,4), dtype= np.complex64) # Complex number, represented by two 32-bit floats
ad = np.zeros ((3,4), dtype= np.complex128) # Complex number, represented by two 64-bit floats

# Basic arrays methods
a.dtype             # returns the array type: int32
b.dtype             # returns the array type: float64
d.dtype             # Returns float64
a.ndim              # Returns array dimensions: 1
c.ndim              # Retruns array dimensions: 2
a.shape             # Returns a tuple with the array shape: (3,)
c.shape             # Retruns a tuple with array shape: (2, 3)

# Numpy constants
np.pi           # pi
np.e            # e


### SCIPY ###

# Using scipy pre-defined constants
from scipy import constants     # Import constants
scipy.constants.pi              # pi
scipy.constants.e               # e
scipy.constants.Avogrado        # Avogrado number

# Some magnitud constants
scipy.constants.kilo            # Kilo 1e3
scipy.constants.mega            # Mega 1e6
scipy.constants.nano            # Nano 1e-9


### PANDAS ###
# Descritpion: Used to import data and manipulate datasets

import pandas as pd         # Standard module import


# Reading datasets
dataframe = pd.read_csv(file)                                   # Imports a CSV file as dataframe
dataframe = pd.read_csv(file, delimiter=r"\s+")                 # Imports a <SPACE> separated file
dataframe = pd.read_csv(file, delim_whitespace=True)            # Imports a <SPACE> separated file
dataframe = pd.read_csv(file, header = None)                    # Imports a file that has no headers
dataframe = pd.read_csv(file, na_filter = False)                # na_filter=False converts all nam into empty strings
dataframe.drop('feature', axis = 1)                             # Eliminates a column 'feature' from the dataframe
                                                                # axis = 0 indicates a row, axis = 1 indicates a column
dataframe = pd.read_csv(file).drop('feature', axis = 1)         # Reads the dataframe and eliminates the column feature


# Create an empty dataframe
dataframe = pd.dataFrame(data = np.nan, index = [0, 1, 2, 3, 4], columns = ['A', 'B'])

# Dataframe manipulation
df1 = dataframe['feature']                          # Creates a new dataframe (df1) with a copy of a feature from dataframe
dataframe = dataframe.replace(np.NaN, 0)            # Replaces all NaN values with 0

dataframe.loc['index1']                             # Returns the row/observation with label <index1>
dataframe.iloc[line]                                # Returns the row/observation of position <line>
dataFrame.iloc[r1:r2]                               # Returns the rows/observations within range <r1>:<r2>
dataFrame.iloc[-1]                                  # Returns the last observation of the datafram

# Convert dataset into numpy array
dataset =  dataframe.values

# Describe the dataset (features, count, mean, std dev, min, etc)
dataframe.describe()

# Desciptive analytics with PANDAS
dataframe.count()           # Count the number of non-null observations
dataframe.sum()             # Sum of values
dataFrame.mean()            # Mean of values
dataframe.mad()             # Mean absolute deviation
dataframe.median()          # Arithmetic median of values
dataframe.min()             # Minimum
dataframe.max()             # Maximum
dataframe.mode()            # Mode
dataframe.abs()             # Absolute value
dataframe.prod()            # Product of values
dataframe.std()             # Bessel-corrected sample standard deviation
dataframe.var()             # Unbiased variance
dataframe.sem()             # Standard error of the mean
dataframe.skew()            # Sample skewness (3rd moment)
dataframe.kurt()            # Sample kurtosis (4th moment)
dataframe.quantile()        # Sample quantile (value at %)
dataframe.cumsum()          # Cumulative sum
dataframe.cumprod()         # Cumulative product
dataframe.cummax()          # Cumulative maximum
dataframe.cummin()          # Cumulative minimum

# This methods can be applied on a particular feature of the dataset
dataFrame['feature'].count()    # Returns the count of non null-observation of 'feature'
dataframe['feature'].mean()     # Retruns the mean of values of 'feature'

