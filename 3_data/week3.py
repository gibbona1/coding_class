#import the pandas library, which has a collection of functions for working with data
#as shorthand, we import it as 'pd'
import pandas as pd 

# Creating the dataset. This is the manual setup
data = {
    "Age": [23, 45, None, 33, 28, 40, 50, 29, 34, 48, 33, 37, 22, 46, 30, 41, 27, 38, 32, 36],
    "Salary": [50000, 80000, 60000, None, 55000, 70000, 90000, 58000, 64000, 85000, 62000, 67000, 52000, 82000, 61000, 73000, 54000, 68000, 63000, 66000],
    "Department": ["HR", "Finance", "IT", "HR", "HR", "Marketing", "Finance", "HR", "IT", "Finance", "IT", "Marketing", "HR", "Finance", "IT", "Marketing", "HR", "Marketing", "IT", "Marketing"]
}

#this converts the object above to a pandas DataFrame
df = pd.DataFrame(data)

#show whole dataset
print(df)

#show first few rows
print(df.head())

#print the number of rows
print(len(df))

#drop any rows with NAs (in python as NaN) present
df = df.dropna()

#alternatively, fill these NAs with some value
#df = df.fillna({'Age': 0, 'Salary': 1000})

#if you used dropna, this might a be different number of rows
#print(len(df))

#sort the data by Age in ascending order
#print(df.sort_values(by='Age'))

#descending order
#print(df.sort_values(by='Age', ascending=[False]))

#show one column
print(df['Salary'])

#show multiple columns (in any order)
print(df[['Salary', 'Department']])

#show all columns in the data
#print(df.columns)

#filtering data
print(df[(df['Age'] >= 40) & 
        (df['Department'] == 'Finance') &
        (df['Salary'] < 85000)
    ])

#check the type of df (should be pandas.core.frame.DataFrame)
#print(type(df))

#check type of the age column (should be pandas.core.series.Series)
#print(type(df['Age']))

#get the average of the salary column
#average_salary = df['Salary'].median()
#print(average_salary)

#average age
#print(int(df['Age'].mean()))
