print("Helo, World!")
#just prints the maths string
print("2+(3*15)=", end="")
#actually evaluates the arithmetic
print(2+(3*15))
#helpful to debugging to see where you are in a program
print("here")
#number of hours/minutes in a leap year
print(60*24*366)
#you can print single quotes inside double quotes or double quotes inside single quotes
print("'To be or not to be' - Hamlet")
print('"To be or not to be" - Hamlet')

## Input from the user
name = input("What is your name? ")

print("your name is " + name + ".")
#the string variable `name` can be overwritten
name = "John"
print("just to double check... your name is " + name + "?")

firstname = input("First name: ")
surname = input("Surname: ")
phone = input("Phone number: ")

print("So your name is " + firstname + " " + surname + " and your phone number is " + phone + ".")

#f-strings are a more modern way to format strings
print(f"So your name is {firstname} {surname} and your phone number is {phone}.")

firstname = "Anthony"
#surname = input("Surname: ")
phone = 112 # not same as "112"

#this will not work because you cannot concatenate a string and an integer
print("So your name is " + firstname + " and your phone number is " + phone + ".")

#this will now work since you've converted `phone`` to a string
print("So your name is " + firstname + " and your phone number is " + str(phone) + ".")
print(f"So your name is {firstname} and your phone number is {phone}.")

