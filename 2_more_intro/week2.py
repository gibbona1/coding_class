name = "John"
age = 20 #integer/int

salary = 123.95 #float

#print(int(4.0 / 2)) #dividing and rounding down to int

#print(int(salary))

#print('mytable1.0.new'.split('.'))

#Boolean
is_weekday = True
is_weekend = False

#print(5 == 4)

#list

my_list = [1, 2, 3, "hello", "apple", True, [1, 2]]

#print(my_list)

my_list.append('new string')

#print(my_list)

extracted_element = my_list.pop(3)
#print(extracted_element)
#print(my_list)

#more things with strings
name = "anthony"
#print(name.upper())
#print(name.lower())
#print(name.capitalize())

#Control structures

#if/else statments
name = 'Anthony'
age = 28
if age == 18:
    print(f"{name} can just about buy alcohol")
elif age > 18:
    print(f"{name} can buy alcohol")
else:
    print(f"{name} can't buy alcohol")

#for loop
numbers = [1, 3, 6, 11, 24]

num = numbers[0]
print(f"number is {num}")
num = numbers[1]
print(f"number is {num}")
print(f"number is {numbers[2]}")
print(f"number is {numbers[3]}")
print(f"number is {numbers[4]}")
print()

for num in numbers:
    print(f"number is {num}")
    print("done with this num")

print()

classroom = ['john', 'mary', 'sean']

for name in classroom:
    print(f"{name} is in the class")
    
print()
#num = 10

for num in [10,9,8,7,6,5,4,3,2,1]:
    print(f'{num} green bottles hanging on the wall,')
    print(f'{num} green bottles hanging on the wall,')
    print('And if one green bottle should accidentally fall,')
    if num == 1:
        print("There'll be no green bottles hanging on the wall.")
    else:
        print(f'There\'ll be {num-1} green bottles hanging on the wall.')
    print()

#functions
#a set of instructions, takes in some inputs and produces an output

def say_hello(name):
    name = name.upper()
    return f'hello, {name}'
print(say_hello('Anthony'))

for person_name in ['Anthony', 'Meg', 'Aibhe']:
    print(say_hello(person_name))

print()

def make_bottle_rhyhme(num_starting_bottles):
    for num in range(num_starting_bottles, 0, -1):
        print(f'{num} green bottles hanging on the wall,')
        print(f'{num} green bottles hanging on the wall,')
        print('And if one green bottle should accidentally fall,')
        if num == 1:
            print("There'll be no green bottles hanging on the wall.")
        else:
            print(f'There\'ll be {num-1} green bottles hanging on the wall.')
        print()
    return 

make_bottle_rhyhme(1)


name = [1,['blah'],3]

for l in name:
    if type(l) is str:
        print(l+'1')
    elif type(l) is list:
        print(l)
    else:
        print(l*500)
    
#print(['a']*5)


#take in list, return two lists, one of positives and one of negatives

int_list = [1,2,-3,10,15,-20,-100]
def find_positive_negative(int_list):
    "take in list, return two lists, one of positives and one of negatives"
    pos_list = []
    neg_list = []
    for el in int_list:
        if el >= 0:
            pos_list.append(el)
        else:
            neg_list.append(el)
    return pos_list, neg_list
    
print(find_positive_negative(int_list))

#list comprehension, efficient one line for loops (usually to filter or transform lists)
pos_list = [el for el in int_list if el>=0]
neg_list = [el for el in int_list if el<0]

print((pos_list, neg_list))
