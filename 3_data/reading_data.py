import pandas as pd

df = pd.read_csv('movie_data.csv')

#SELECT movie_table from my_database

#API
#curl/python

df_sub = df[df['Year'] == 2024]
df_sub[df_sub['Runtime (mins)'] > 120][['Title', 'Runtime (mins)']]