# Chapter 3.1 Introduction, no code
# Chapter 3.2 Conditional Statements
# Seth Fry

# Chapter 3.2 - Mosh Ebook
temperature = 15
if temperature > 30:
    print("It's Warm")
    print("Drink Water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done.")
# Pretty simple if|elif|else statment here

# Chapter 3.3 - Mosh Ebook

age = 12
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
# The if else that is above this comment is not neccesarily clean code, but it works.
# Use a ternary operator (below) when possible
message = "Eligible" if age >= 18 else "Not eligable"
print(message)

# Chapter 3.4 - Mosh Ebook

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
# Putting the first 2 in parenth is a good way to seperate before you use the not operator

# Chapter 3.5 - Mosh Ebook
# Short-circuit Evaluation
high_income = False
good_credit = True
student = True

if (high_income or good_credit) or not student:
    print("Eligible")
else:
    print("Not eligible")
# Basically short-circuit evaluation goes through the expression piece by piece to evaluate and when it determines that its true it has not need to go any further
# In this example it sees that high_income is false and continues to good_credit. After it sees good_credit is true, it will just skip the student logical operator

# Chapter 3.6
# Chaining Comparison Operators

# age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print("Eligible")

if 18 <= age < 65:
    print("Eligible")

# Even though they are written differently - These mean the same thing
# The second one is just using math
\


