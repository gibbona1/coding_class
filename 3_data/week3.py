import pandas as pd 

# Creating the dataset
data = {
    "Age": [23, 45, None, 33, 28, 40, 50, 29, 34, 48, 33, 37, 22, 46, 30, 41, 27, 38, 32, 36],
    "Salary": [50000, 80000, 60000, None, 55000, 70000, 90000, 58000, 64000, 85000, 62000, 67000, 52000, 82000, 61000, 73000, 54000, 68000, 63000, 66000],
    "Department": ["HR", "Finance", "IT", "HR", "HR", "Marketing", "Finance", "HR", "IT", "Finance", "IT", "Marketing", "HR", "Finance", "IT", "Marketing", "HR", "Marketing", "IT", "Marketing"]
}

df = pd.DataFrame(data)
#print(len(df))
#df = df.dropna()
#df = df.fillna({'Age': 0, 'Salary': 1000})
#print(len(df))

#print(df.sort_values(by='Age'))

print(df[['Salary', 'Department']])
#print(df)

#print(len(df))

#print(df['Age'])

#print(df.columns)

#print(df.head(2))

#print(df[(df['Age'] >= 40) & 
#        (df['Department'] == 'Finance') &
#        (df['Salary'] < 85000)
#    ])
    
#print(type(df['Age']))
#average_salary = df['Salary'].median()
#print(average_salary)

#average age
#print(int(df['Age'].mean()))

