# Practice Questions

## Q1

Write a function `make_line` that takes in two arguments: `word` (a string) and `n` (an integer)
so that it returns the `word` repeated `n` times (and makes it into a kind of line).
e.g. 
`make_line('hello', 3)` should return `hellohellohello`
`make_line('a', 10)` should return `aaaaaaaaaaa`
As a bonus, check that `word` is a `str` and `n` is an `int`, and print an error if so.

<details>
  <summary>Hint</summary>
  
  Example check for `n`: 
  ```
  if type(n) is str: 
    print('oops, n is string!')
    return
  ```
</details>

## Q2

write a function `greet_many_times` that takes a `name` and greets them `n` times, each on a new line.
e.g. `greet_many_times('John', 3)` should return
```
Hello, John!
Hello, John!
Hello, John!
```
As a bonus, check that `name` is a `str` and `n` is an `int` greater than zero.

<details>
  <summary>Hint</summary>
  
  `['blah']*3` would create `['blah', 'blah', 'blah']`
  and `'\n'.join(['blah', 'blah', 'blah'])` will make the string
  ```
  blah
  blah
  blah
  ```
</details>

## Q3

Write a function `add_initial` which takes a person's `name` (in the form `firstname surname`, separated by a space), and an `initial` (one letter/chaaracter)
add an extra argument `add_dot`, which should be made `True` by default, that adds a full stop to the initial.
e.g. 
`add_initial('Samuel Jackson', 'L')` returns `Samuel L. Jackson`
`add_initial('Vivica Fox', 'A')` returns `Vivica A. Fox`
`add_initial('Michael Higgins', 'D', add_dot = False)` returns `Michael D Higgins`
As a bonus, ensure `initial` is just one letter, and make sure each `word` in the final answer is capitalised.

<details>
  <summary>Hint</summary>
  
  `'A' + '.' = 'A.'`

  `'joe bloggs'.split(' ')` would give  `['joe', 'bloggs']`
  
  And if we have `my_list = ['joe', 'bloggs']`
  then `my_list.insert(1, 'A')` updates `my_list` to `['joe', 'a', 'bloggs']` (it inserts `A` at index 1).
</details>
