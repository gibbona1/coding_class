import pandas as pd

#reading from database
##SELECT movie_table from my_database

#or from an API, where you give instructions to a URL to get data, using curl/python
##curl -G "https://api.example.com/data" -d "param1=value1" -d "param2=value2"

#read from csv
df = pd.read_csv('movie_data.csv')

#filter to just those films released in 2024
df_sub = df[df['Year'] == 2024]
#df_sub[df_sub['Runtime (mins)'] > 120][['Title', 'Runtime (mins)']]

#save filtered data to CSV (ensure it's a different name)
df_sub.to_csv('movie_data_2024.csv')