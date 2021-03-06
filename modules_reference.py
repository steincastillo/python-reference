'''
Python Modules Quick Reference

https://github.com/steincastillo/python-reference.git
Edited by: Stein Castillo
http://www.stein-castillo.com

Table of Contents:
    numpy
    scypi
    pandas
    matplotlib
    regular expressions
    sqlite
    io
'''

### NUMPY ###
# Description: Provides advance functionality to operate and manipualte arrays
# Additional documentation can be found at: https://docs.scipy.org/doc/numpy/index.html
# Additional reference can be found at: https://docs.scipy.org/doc/numpy/reference/index.html

import numpy as np  # standard module import

# Creating numpy arrays
a = np.array([2, 3, 4])                 # Creates a single numpy array. values must be passed as a list
b = np.array([1.2, 3.5, 5.1])           # Creates a numpy array
c = np.array([[1, 2, 3],  [4, 5, 6]])    # Creates a 2 dimensional array
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

# Numpy notation to access the array
nd1 = np.array([[1, 2, 3, 4],  [4, 5, 6, 7]], np.int32)    # Creates a 2 dimensional array
# Numpy notation to access array: nd1[row, col] 
# Numpy arrays are 0 base index
nd1[0, 0]           # Returns 1 (column 0, row 0)
nd1[1, 0]           # Returns 4 (column 1, row 0)
nd1[-1, :]          # Returns the last row and all the columns
nd1[:, 2]           # Returns all the rows column 2
nd1[1, :]           # Returns column 1 all the rows


array = np.asarray(list)                    # Convert list to array
list = array.tolist()                       # Convert array to list

array = array[::-1]                         # Reverses array

# Basic arrays methods
a.dtype             # returns the array type: int32
b.dtype             # returns the array type: float64
d.dtype             # Returns float64
a.ndim              # Returns array dimensions: 1
c.ndim              # Returns array dimensions: 2
a.size              # Returns the number of elements in the array
a.shape             # Returns a tuple with the array shape: (3,)
c.shape             # Returns a tuple with array shape: (2, 3)
c.shape[0]          # Returns the number of rows in the array
c.shape[1]          # Returns the number of columns in the array

# Operation on arrays
# Sum
a.sum()             # Returns the sum of the elements of the array
a.sum(axis=0)       # Returns the sum of the columns in the array
a.som(axis=1)       # Returns the sum of the rows in the array
# minimum/maximum values
a.min()             # Returns the minimun value in the array
a.min(axis=0)       # Returns the minimum value of each column
a.min(axis=1)       # Returns the minimun value of each row
a.max()             # Returns the maximum value of the array
a.max(axis=0)       # Returns the maximum value of each columna
a.max(axis=1)       # Returns the maximum value of each row
a.argmax()          # Returns the index of the maximum value
# Mean
a.mean()            # Returns the mean value of the array
a.mean(axis=0)      # Returns the mean of each column
a.mean(axis=1)      # Returns the mean of each row

# Numpy constants
np.pi           # pi
np.e            # e

#############
### SCIPY ###
#############

# Using scipy pre-defined constants
from scipy import constants     # Import constants
scipy.constants.pi              # pi
scipy.constants.e               # e
scipy.constants.Avogrado        # Avogrado number

# Some magnitud constants
scipy.constants.kilo            # Kilo 1e3
scipy.constants.mega            # Mega 1e6
scipy.constants.nano            # Nano 1e-9

# Create random gaussian data sample
sample = np.random.normal(center, std_deviation, size)
# Example:
sample = np.random.normal(0, 2, 20) # Gaussian sample, center 0, standard deviation 2, 20 numbers

# Create evenly spaced interval
interval = np.linspace(start, stop, number, dtype=type)
# Example:
interval = np.linspace(0, 10, 11, dtype=int)    # Returns an interval of ints from 0 to 10 -> [0..10]

##############
### PANDAS ###
##############

# Description: Used to import data and manipulate dataframes

import pandas as pd         # Standard module import

# Reading datasets
dataframe = pd.read_csv(file)                                   # Imports a CSV file as dataframe
dataframe = pd.read_csv(file, delimiter=r"\s+")                 # Imports a <SPACE> separated file
dataframe = pd.read_csv(file, delimiter='|')                    # Imports a | separated file. 
dataframe = pd.read_csv(file, delim_whitespace=True)            # Imports a <SPACE> separated file
dataframe = pd.read_csv(file, header = None)                    # Imports a file that has no headers
dataframe = pd.read_csv(file, na_filter = False)                # na_filter=False converts all nam into empty strings
dataframe = pd.read_csv(file, encoding = 'utf-8')               # imports a CSV file setting the encoding to utf-8. 
                                                                # other encoding options: utf-16, latin

dataframe.drop('feature', axis = 1)                             # Eliminates a column 'feature' from the dataframe
                                                                # axis = 0 indicates a row, axis = 1 indicates a column
# Managing missing information
dataframe.dropna()                                              # Eliminate all NaN observations
dataframe.fillna(0)                                             # Replace all NaN values with 0. A different value can be specified
datafrane.fillna(method='ffill')                                # NaN values forward filling
dataframe.fillna(method='backfill')                             # NaN values backward filling
                                                                
dataframe = pd.read_csv(file).drop('feature', axis = 1)         # Reads the dataframe and eliminates the column feature
dataframe = pd.DataFrame(list)                                  # Convert an existing dictionary into a dataframe
    
dataFrame = pd.read_json(file.json)                             # Imports a JSON file as dataframe

# Create an empty dataframe
dataframe = pd.DataFrame(data = np.nan, index = [0, 1, 2, 3, 4], columns = ['A', 'B'])

# Insert a column in a specific location
dataFrame.insert(loc=2, column='A', value=0)        # Inserts a column named A on the after the 2nd column with value 0

# Reaname a column in dataframe
dataFrame = dataFrame.rename(columns={'old name1':'new name1', 'old name2':'new name2'})

# Delete a column in the dataframe
dataFrame = dataFrame.drop(['column'], axis=1)

# Get the index of a column
dataFrame.columns.get_loc('column')                 # Returns the index of column

# Reverse a dataframe
dataframe.iloc[::-1]

# Reset the index of a dataframe
dataframe.reset_index(drop=True, inplace=True)

# Dataframe slicing
df1 = dataframe['feature']                          # Creates a new dataframe (df1) with a copy of a feature from dataframe
dataframe = dataframe.replace(np.NaN, 0)            # Replaces all NaN values with 0

dataframe.loc['index1']                             # Returns the row/observation with label <index1>
dataframe.iloc[line]                                # Returns the row/observation of position <line>
dataFrame.iloc[r1:r2]                               # Returns the rows/observations within range <r1>:<r2>
dataFrame.iloc[-1]                                  # Returns the last observation of the dataframe
dataframe['feature'].iloc[-1]                       # Returns the last observation of the specific feature

dataframe['feature'].unique()                       # Lists unique values in a dataframe column
len(dataframe.index)                                # Quick count of rows in a dataframe
dataframe.column_name = dataframe.column_name.astype(float) # Converts values of a column to type float

dataframe['feature'].tolist()                       # Converts the values of the feature to a list

# Split delimited values in Dataframe column into two new columns
df['new_col1'], df['new_col2'] = zip(*df['original_col'].apply(lambda x: x.split(',', 1)))

# Search values in a dataframe
idx = dataframe.index[dataframe['feature']==value]  # Returns the index where the value is found
value = dataframe[dataframe['feature']==value]      # Returns a dataframe with the values where the condition is true

# Convert dataset into numpy array
dataset =  dataframe.values

# Get quick count of rows/columns in a DataFrame
len(dataframe.index)
len(dataFrame.columns)

# iterate over the rows of a dataframe
for index, row in dataframe.iterrows():
    print (row)
    print (row['index1'], row['index2'])

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
dataframe['feature'].mean()     # Returns the mean of values of 'feature'

# Ploting a dataframe
dataFrame.plot()            # Plots the content of the dataframe
dataFrame.plot(grid=True)   # Plost the dataframe and adds a grid to the chart
ax = dataFrame.plot()       # Creates a pyplot chart
ax.set(title='Title', xlabel='x axis label', ylabel='y axis label') # Set chart properties
# Other chart examples
ax = dataFrame.plot(title='Title', linewidth=2.5)
ax = dataFrame.hist()           # Plots a histogram
ax = dataFrame.hist(bins=20)    # Plots a histogram with 20 bins

##################
### MATPLOTLIB ###
##################

'''
Used to produce charts. Works well with pandas dataframe and numpy arrays

More information:
https://matplotlib.org/index.html
'''

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter # Module support configurable tick locating and formatting

# Basic line chart 
fig, ax = plt.subplots()    # Create figure
ax.plot(xdata, ydata)       # plot data
# Set chart properties
ax.set(xlabel='x label', ylabel='y label', title='Chart Title')
ax.grid()   # Diplay chart grid standard parameters
ax.grid(color='r')  # Red color grid

# Formatting the plot
print(plt.style.available)      # Print the available formatting styles
plt.style.use('fivethirtyeight')    # Apply formatting style
lables = ax.get_xticklabels()       # Get x axis labels attributes
plt.setp(labels, rotation=45)       # Set xlabels rotation to 45 degrees
# set xlabel font size:
plt.xlabel ('xlabel', fontsize=10)  # Method 1
plt.setp(labels, fontsize=10)       # Method 2

# Adding elements to the chart
ax.axvline(xvalue)      # Draw a vertical line at xvalue
ax.axhline(yvalue)      # Draw a horizontal line at yvalue

# Colors and formatting elements
'''
Colors
    b: Blue
    g: Green
    r: Red
    c: Cyan
    m: Magenta
    y: Yellow
    w: White

Line style
    :  .......
    -. --.--.--.
    -- ---------
    -

Markers
    . Point
    , Pixel
    o Circle
    v Triangle down
    ^ Triangle up
    < Triangle left
    > Triangle right
    1 Tri down
    2 Tri up
    3 Tri left
    4 Tri right
    8 Octagon
    s Square
    p Pentagomn
    s Star
    h Hexagon1
    H Hexagon2
'''

###########################
### Regular Expressions ###
###########################

import re       # import the regular expressions module

'''
Regular expression wildcards symbols:
* : Zero or more
? : Zero or one
+ : one or more
. : Matches any character except new line
^ : Begins with
$ : Ends with
\w: Matches word characters
\S: Matches any non-whitespace character
\B: Matches the string withing the \B \B boundary
'''

# Search patterns
re.search(patterns, text)   # Searchs for a pattern in a text. returs True or False

# zero or one pattern
# ab? menas 'a' followed by zero or one 'b'
re.search('ab?', 'ac')      # Returns True. Means 'a' followed by zero or one 'b'
re.search('ab?', 'abc')     # Returns True. Means 'a' followed by zero or one 'b'
re.search('ab?', 'abbc')    # Returns True. Means 'a' followed by zero or one 'b'

# Zero or more pattern
# ab* means 'a' followed by zero or more 'b'
re.search('ab*', 'ac')      # Returns True. Means 'a' followed by zero or more 'b'
re.search('ab*', 'abc')     # Returns True. Means 'a' followed by zero or more 'b'
re.search('ab*', 'abbc')    # Returns True. Means 'a' followed by zero or more 'b'

# one or more pattern
# ab+ menas 'a' followed by one or more 'b'
re.search('ab+', 'ac')      # Returns False. Means 'a' followed by one or more 'b'
re.search('ab+', 'abc')     # Returns True. Means 'a' followed by one or more 'b'
re.search('ab+', 'abbc')    # Returns True. Means 'a' followed by one or more 'b'

# Exact pattern
# ab{2} means 'a' followed exactly by 2 'b'
re.search('ab{2}', 'ac')    # Returns False. ab{2} means 'a' followed exactly by 2 'b'
re.search('ab{2}', 'abc')   # Returns False. ab{2} means 'a' followed exactly by 2 'b'
re.search('ab{2}', 'abbc')  # Returns True. ab{2} means 'a' followed exactly by 2 'b'

# Pattern at start and end
# ^a means starts with 'a'
# .* means zero or more occurrences of any character
# c$ means end with 'c'
# ^a.*c$ means start with 'a' followed by zero or more characters and end with 'c'

re.search('^a.*c$', 'abbc') # Returns true

# Pattern to test the beginning of a word
# ^\w+ means starts with any alphanumeric character and one or more occurrences of it
re.search('^\w+', 'abbc')   # Returns True

# Pattern to test the end of a word
# \w+\S*?$ means any alphanumeric character with non-whitespace at the end
re.search('\w+\S*?$', 'Loli eats peas') # Returns True

# Pattern to find a word that contains a specific character
# \Bu\B matches the 'u' character withing the \B \B boundary
print (text_match('Tuffy eats pie, Loli eats peas!', '\Bu\B'))  # Returns True

# Search for a pattern and its location
text = 'Diwali is a festival of lights, holi is a festival of colors!'
pattern = 'festival'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print ('Found {} at {}:{}'.format(text[s:e], s, e))


# Substitutions
street = '21 Ramakrishna Road'
print (re.sub('Road', 'Rd', street)) # Returns 21 Ramakrishna Rd


##############
### SQLITE ###
##############

# Description: Light weight database manager

# Common sqlite statements - Cannot be directly used in python!

# Data definition language (CREATE, ALTER, DROP)

# Create table
CREATE TABLE comments (
    post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    website TEXT NOT NULL,
    comment TEXT NOT NULL);

# Add new columns (Alter)
ALTER TABLE comments ADD COLUMN username text;

# Delete a table (Drop)
DROP TABLE comments;

# Create view
CREATE VIEW [IF NOT EXISTS] view_name (column-name-list)
AS 
    select-statement;

CREATE VIEW IF NOT EXISTS v_coins as 
    SELECT
        name as country,
        value,
        year,
        currency
    FROM
        coins;

# Remove a view
DROP VIEW [IF EXISTS] view_name;

DROP VIEW v_coins;

# Data manipulation language (INSERT, UPDATE, DELETE)

# Insert rows
INSERT INTO comments (name, email, website, comment)
VALUES ('test_name', 'test@email.com', 'test website', 'test comment');

# Update rows
UPDATE comments set email = 'new@mail.com' WHERE name = 'test_name';
UPDATE comments set email = 'new@mail.com' WHERE post_id = 1;

# Delete rows
DELETE FROM comments WHERE post_id = 1;
DELETE FROM comments WHERE name = 'test_name';

# Join tables
SELECT
    name as country,
    value,
    year,
    currency
FROM
    coins
INNER JOIN country on country.iso = coins.country
ORDER BY year;

# Data query language (SELECT)

SELECT post_id, name, email, website, comment FROM comments;
SELECT * FROM comments;

# Using SQLITE in python

# Standard import
import sqlite3

# Open DB connection
conn = sqlite3.connect('mydatabase.db') # Opens the specified file
conn = sqlite3.connect(:memory:) # Creates de database in RAM

# open DB connection READ ONLY
conn = sqlite3.connect('file:mydatabase.db?mode=ro', uri=True)

# Executing SQLITE commands
# A cursor object needs to be created to execute the commands
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE albums
                (title TEXT, 
                artist TEXT, 
                release_date TEXT,
                publisher TEXT,
                media_type TEXT)''')

# Insert data
cursor.execute('''INSERT INTO albums VALUES(
                'Glow', 
                'Andy Hunter',
                '7/24/12',
                'Xplore Records',
                'MP3')''')

# Insert data using the more secure "?" method
album = [('Exodous', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD')]

cursor.execute('INSERT INTO albums VALUES (?, ?, ?, ?, ?)', album)

# Display table contents formated
import pandas as pd
print (pd.read_sql_query('SELECT * FROM table;', conn))
# Load DB into a dataframe
df = pd.read_sql_query('SELECT * FROM table', conn)

##########
### io ###
##########

import io

# Read a text file with specific encoding
with io.open(filename, 'r', encoding='utf-8') as f:
    text = f.read()
f.close()
