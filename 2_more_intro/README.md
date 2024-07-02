# 2. More introduction

Data types, control structures and writing functions

A little extra to continue from last week

## 2.0 Data types and Control Structures

### Data Types

#### Integers

Whole numbers, positive or negative, without a fractional part.

```
my_int = 42
```

#### Floats

Numbers that contain a decimal point, representing fractional values.

```
my_float = 3.14
```


#### Booleans

Logical data type with two possible values: `True` or `False`.

```
my_bool = True
```

#### Lists

Ordered, mutable collection of items. Items can be of different data types.
```
my_list = [1, 2, 3, 'apple', 'banana']
```

You can append to a list easily

```
my_list.append('hello')
print(my_list)
```

And you can extract one element of the list
```
#python is zero-indexed, so the first item is item 0, second item is item 1, etc
print(list[0])
#last item is item -1, second last is -2, etc
print(list[-1])
```


#### Strings
Ordered, immutable sequence of characters.
```
my_string = "Hello, World!"
```

concatenate two strings together
```
firstname = 'john'
surname = 'doe'
print(firstname + ' ' + lastname)
```

```
# Convert a string to uppercase
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