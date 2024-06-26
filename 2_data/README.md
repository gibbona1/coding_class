## 2. Data

A little extra to continue from last week

### 2.0 Control Structures

manipulation, concatination, indexing, logic

if/else

for loops

writing functions

### Data Formats

csv/excel

JSON

txt

### Data Sources (local tabular files, APIs, databases)


#### Local files

Data stored on your computer or network drives.
Examples: CSV, Excel, JSON, TXT files.

#### Application Programming Interfaces (APIs) 

Allow you to access data from web services.
Common in retrieving real-time data from websites and services.


#### Databases

Structured storage systems for large volumes of data.
Examples: SQL databases (MySQL, PostgreSQL), NoSQL databases (MongoDB).

### Data reading and manipulation 

In python, 99% of your data reading and manipulation will be done using the pandas library.

A library is just a collection of classes (e.g. DataFrames which store your data) and functions (things to do to the data)

the common way to load this library is

```import pandas as pd```

This means any time you want to use a function/class from the pandas library, you write `pd.function_name()` od `pd.Class()`

SO, to load an excel file called `my_data.csv`, you write

```df = pd.read_csv('my_data.csv')```

the df object is a `pd.DataFrame`, it should look familiar enough to excel

