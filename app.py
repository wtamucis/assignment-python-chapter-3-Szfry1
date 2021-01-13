# Chapter 3.1 Introduction, no code
# Chapter 3.2 Conditional Statements
# Seth Fry

# Chapter 3.2 - Mosh Ebook
print("Chapter 3.2 Conditional Statements")
temperature = 15
if temperature > 30:
    print("It's Warm")
    print("Drink Water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done.")
print("*" * 30)
# Pretty simple if|elif|else statment here

# Chapter 3.3 - Mosh Ebook
print("Chapter 3.3 Ternary Operator")
age = 12
# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"
# The if else that is above this comment is not neccesarily clean code, but it works.
# Use a ternary operator (below) when possible
message = "Eligible" if age >= 18 else "Not eligable"
print(message)

cost = 300
status = "expensive" if cost > 100 else "cheap"
print(status)
print("*" * 30)

# Chapter 3.4 - Mosh Ebook
print("Chapter 3.4 Logical Operators")

# Three logical operators in python

# and
# or
# not

# Remember that python is case sensitive

high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
print("*" * 30)
# Putting the first 2 in parenth is a good way to seperate before you use the not operator

# Chapter 3.5 - Mosh Ebook
print("Chapter 3.5 - Short-circuit Evaluation")

high_income = False
good_credit = True
student = True

if (high_income or good_credit) or not student:
    print("Eligible")
else:
    print("Not eligible")
# Basically short-circuit evaluation goes through the expression piece by piece to evaluate and when it determines that its true it has not need to go any further
# In this example it sees that high_income is false and continues to good_credit. After it sees good_credit is true, it will just skip the student logical operator
print("*" * 30)
print("Chapter 3.6 Chaining Comparison Operators")

# age should be between 18 and 65
age = 22
# if age >= 18 and age < 65:
#     print("Eligible")

if 18 <= age < 65:
    print("Eligible")

print("*" * 30)

# Even though they are written differently - These mean the same thing
# The second one is just using math

# 3.7 QUIZ

# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")

# this should print c when ran

print("Chapter 3.8 - For Loops")

# print("Sending a message")

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# A cleaner version of this that uses the range function looks like this below


for number in range(1, 4):  # You can add a step here by adding a third arguement
    print("Attempt", number, (number) * ".")

#How to Count by twos
for number in range (1 , 10 , 2):
    print("Attempt", number + 1 , (number + 1) * ".")
#How to count down from 10 to zero 
for number in range (10, 0, -1):
    print(number)
print("*" * 30)

print("3.9 For-Else Loops")

# if failed
successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed.")
#If Successful

successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed.")

print("*" * 30)
print("Chapter 3.10 Nested Loops")
for x in range(5):
    for y in range(3):
        print(f"{x}, {y}")
print("*" * 30)

print('3.11 iterables')
# print(type(5))
# print(type(range(4)))
for x in [1,2,3,4]:
    print(x)

print("*" * 30)


print('3.12 While loops')
# number = 100
# while number > 0:
#     print(number)
#     number //= 2
command = ""
while command != "quit":
    command = input("Enter any command or 'quit' >")
    print("ECHO", command)
print("*" * 30)

#3.13 
#Infinite Loops

while True:
    command = input("Enter any command or 'quit' >")
    print("ECHO", command)
    if command.lower() == "quit":
        break
print("*" * 30)

#3.14 Exercise
counter = 0
for num in range(1, 10):
    if num % 2 == 0:
        print(num)
        counter += 1
print(f"You have {counter} even numbers.")
print("*" * 30)



    
