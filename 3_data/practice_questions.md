# Practice Questions

First load the pandas library

```
import pandas as pd
```

now load the data

```
df = pd.read_csv('movie_data.csv')
```

Answer the following questions:

## Q1

- How many rows in this dataset? 
- How many movies in this dataset?

<details>
  <summary>Hint</summary>
  
  Check `Title Type` column. 
  It's worth filtering to get the movies and store this as a new `df`
</details>

## Q2

- How many films from 2024?
- How many movies between 1990 and 1999 inclusive?

## Q3

- What is the longest film in the dataset?
- When was it rated?

<details>
  <summary>Hint</summary>
  
  use `.sort_values` method here, `ascending = [False]`
</details>

## Q4

- What is the average rating of everything in the data?
- What about the average for TV Shows?
- What about just films directed by Cheistopher Nolan?

## Q5

- What are the top 7 movies on the lst by IMDb Rating?
- What movie had the most votes?

<details>
  <summary>Hint</summary>
  
  `.sort_values` and `.head()` useful here
</details>

## Q6

- How many movies rated in 2021? (between 01/01/2021 and 31/12/2021 inclusive)

<details>
  <summary>Hint</summary>
  
  filtering dates uses `>`,`>=`,`<`,`<=` like with numbers
</details>

## Q7

- How many movies directed by Danny Boyle were rated in 2023?
- How many of them are longer than 100 mins?

## Q8

- What's the highes rated movie in 2023 that didn't come out in 2023?

## Q9

For each of these directors, `['Denis Villeneuve','Céline Sciamma','Yasujirō Ozu']`, find:

- Their average IMDb rating
- Their average rating by me
- Their most recent movie
- The combined number of votes for their films


