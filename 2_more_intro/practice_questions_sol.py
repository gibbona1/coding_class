def greet_many_times(name, n):
    for i in range(n):
        print(f'Hello, {name}!')
    return

#greet_many_times('John', 3)

def add_initial(name, initial, add_dot = False):
    name_split = name.split(' ')
    first_name = name_split[0]
    surname = name_split[1]
    if add_dot:
        return f'{first_name} {initial}. {surname}'
    else:
        return f'{first_name} {initial} {surname}'

#for i in range(10):
#    print(add_initial('Michael Higgins', 'D', add_dot = True))
#    print()

from math import sqrt

#check if number is a square number
#print(sqrt(100) == int(sqrt(100)))

def only_squares(a):
    res = []
    for i in a:
        if sqrt(i) == int(sqrt(i)):
            res.append(i)
    return res

print(only_squares([1,2,4,6,9]))

def only_squares2(a):
    return [i for i in a if sqrt(i) == int(sqrt(i))]

print(only_squares2([1,2,4,6,9]))