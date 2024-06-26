# 2. Data

A little extra to continue from last week

## 2.0 Data types and Control Structures

### Data Types

Lists: Ordered, mutable collection of items. Items can be of different data types.
```
my_list = [1, 2, 3, 'apple', 'banana']
```

You can append to a list easily

```
my_list.append('hello')
print(my_list)
```



Strings: Ordered, immutable sequence of characters.
```
my_string = "Hello, World!"
```

Tuples: Ordered, immutable collection of items. Items can be of different data types.
```
my_tuple = (1, 2, 3, 'apple', 'banana')
```

### string manipulation

```
# Convert the string "hello" to uppercase
s = "hello"
s_upper = s.upper()
print(s_upper)
```

### if/else

This is the cornerstone of basic programming logic. 
When a certain condition or set of conditions is true, do something, otherwise, do something else

```
age = 100
if age >= 18:
    print('you can drink')
else:
    print('you can\'t drink!')
```

### for loops

Another common feature of programs is the for loop.

A for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range).

It allows you to execute a block of code multiple times, once for each item in the sequence.

```
# Print each number in the list [10, 20, 30, 40, 50]
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)
```

```
# Print each character in the string "Python"
word = "Python"
for char in word:
    print(char)
```

Exercise: write a for loop that would print out the ten green bottle nursery rhyme (https://en.wikipedia.org/wiki/Ten_Green_Bottles)
```
for i in range(10, 0, -1):
    print(f"{i} green bottles hanging on the wall,")
    print(f"{i} green bottles hanging on the wall,")
    print("And if one green bottle should accidentally fall,")
    if i == 1:
        print("There'll be no green bottles hanging on the wall.")
    else:
        print(f"There'll be {i-1} green bottles hanging on the wall.")
    print()  # Print a blank line between verses
```


### writing functions

Say we have the following code to multiply two given numbers

```
# Multiply 7 by 8
a = 7
b = 8
product = a * b
print('The product is:', product)
```

What if we wanted a small function that would take in any two numbers we give it and return the sentence `The product is: x`

```
def multiply_nums(a, b):
    product = a*b
    return f'The product is: {product}'
```

Exercise: complete this function (help here https://www.almanac.com/when-next-leap-year)

```def is_leap_year(year):
    #return 'yes' if leap year, else 'no'
    return ''
```

Exercise: redo the ten green bottles exercise but for an arbitrary number of starting bottles

## 2.1 Data Formats

csv/excel

JSON

txt

## 2.2 Data Sources (local tabular files, APIs, databases)


### Local files

Data stored on your computer or network drives.
Examples: CSV, Excel, JSON, TXT files.

### Application Programming Interfaces (APIs) 

Allow you to access data from web services.
Common in retrieving real-time data from websites and services.


### Databases

Structured storage systems for large volumes of data.
Examples: SQL databases (MySQL, PostgreSQL), NoSQL databases (MongoDB).

## 2.3 Data reading and manipulation 

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