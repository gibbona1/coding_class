# 3. Data

## 3.1 Data Formats

csv/excel

JSON

txt

## 3.2 Data Sources (local tabular files, APIs, databases)


### Local files

Data stored on your computer or network drives.
Examples: CSV, Excel, JSON, TXT files.

### Application Programming Interfaces (APIs) 

Allow you to access data from web services.
Common in retrieving real-time data from websites and services.


### Databases

Structured storage systems for large volumes of data.
Examples: SQL databases (MySQL, PostgreSQL), NoSQL databases (MongoDB).

## 3.3 Data reading and manipulation 

In python, 99% of your data reading and manipulation will be done using the pandas library.

A library is just a collection of classes (e.g. DataFrames which store your data) and functions (things to do to the data)

the common way to load this library is

```
import pandas as pd
```

This means any time you want to use a function/class from the `pandas` library, you write `pd.function_name()` od `pd.Class()`

So, to load an excel file called `my_data.csv`, you write

```
df = pd.read_csv('my_data.csv')
```

the df object is a `pd.DataFrame`, it should look familiar enough to excel

take this example dataset

```
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)
print(df)
```

You can manipulate this data

### Select the 'Name' column
```
names = df['Name']
print(names)
```

### Filter rows where Age is greater than 30
```
filtered_df = df[df['Age'] > 30]
print(filtered_df)
```

### Calculate the average Salary
```
average_salary = df['Salary'].mean()
print("Average Salary:", average_salary)
```

### Add a row with missing values
```
df_with_nan = df.append({'Name': 'Frank', 'Age': None, 'Salary': None}, ignore_index=True)
print("DataFrame with NaN values:\n", df_with_nan)
```

### Drop rows with any missing values
```
cleaned_df = df_with_nan.dropna()
print("DataFrame after dropping NaN values:\n", cleaned_df)
```

### Fill missing values with a specified value
```
filled_df = df_with_nan.fillna({'Age': 0, 'Salary': 0})
print("DataFrame after filling NaN values:\n", filled_df)
```