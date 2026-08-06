"""
==========================================================
PYTHON VARIABLES - COMPLETE BEGINNER GUIDE
==========================================================


# ==========================================================
# 1. WHAT IS A VARIABLE?
# ==========================================================

# A variable is a name that refers to a value.
#
# Think of a variable like a labeled box.
#
# Example:
#
# name  ---> "Shubham"
# age   ---> 28
#
# Here:
# name = variable name
# "Shubham" = value

name = "Shubham"
age = 28

print(name)
print(age)


# ==========================================================
# 2. CREATING VARIABLES
# ==========================================================

# Syntax:
#
# variable_name = value
#
# The = symbol is called the assignment operator.
#
# It assigns the value on the RIGHT
# to the variable name on the LEFT.

name = "Shubham"
city = "Mumbai"
age = 28

print(name)
print(city)
print(age)


# ==========================================================
# 3. WHY DO WE USE VARIABLES?
# ==========================================================

# Without a variable:

print("Shubham")
print("Shubham")
print("Shubham")

# Instead, we can store the value once:

name = "Shubham"

print(name)
print(name)
print(name)

# If we want to change the name,
# we only need to change the variable value.


# ==========================================================
# 4. DIFFERENT TYPES OF VARIABLES
# ==========================================================


# ----------------------------------------------------------
# STRING (str)
# ----------------------------------------------------------

# Strings are used to store text.
# Strings are written inside quotes.

name = "Shubham"
city = "Mumbai"
job_role = "Data Analyst"

print(name)
print(city)
print(job_role)


# ----------------------------------------------------------
# INTEGER (int)
# ----------------------------------------------------------

# Integers are whole numbers.
# They do not contain decimal points.

age = 28
salary = 70000
year = 2026

print(age)
print(salary)
print(year)


# ----------------------------------------------------------
# FLOAT (float)
# ----------------------------------------------------------

# Floats are numbers containing decimal points.

height = 5.8
price = 99.99
temperature = 36.5

print(height)
print(price)
print(temperature)


# ----------------------------------------------------------
# BOOLEAN (bool)
# ----------------------------------------------------------

# Boolean values can only be:
#
# True
# False

is_learning_python = True
is_married = False

print(is_learning_python)
print(is_married)

# Important:
#
# Correct:
# True
# False
#
# Incorrect:
# true
# false


# ==========================================================
# 5. CHECKING THE DATA TYPE
# ==========================================================

# Python provides the type() function.
#
# type() tells us what kind of data
# a variable contains.

name = "Shubham"
age = 28
height = 5.8
is_employee = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_employee))

# Output:
#
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>


# ==========================================================
# 6. PYTHON AUTOMATICALLY DETECTS DATA TYPES
# ==========================================================

# We do not normally need to tell Python
# the data type when creating a variable.

name = "Shubham"       # Python understands this is str
age = 28               # Python understands this is int
salary = 70000.50      # Python understands this is float
is_employee = True     # Python understands this is bool

print(type(name))
print(type(age))
print(type(salary))
print(type(is_employee))

# Python is a dynamically typed language.


# ==========================================================
# 7. VARIABLES CAN CHANGE
# ==========================================================

# A variable can be reassigned to another value.

age = 27

print(age)

# Reassigning the variable

age = 28

print(age)

# Output:
#
# 27
# 28

# The latest assigned value is used.


# ==========================================================
# 8. VARIABLE NAMING RULES
# ==========================================================


# ----------------------------------------------------------
# RULE 1: Use letters
# ----------------------------------------------------------

name = "Shubham"
age = 28


# ----------------------------------------------------------
# RULE 2: Numbers are allowed
# but the variable cannot START with a number
# ----------------------------------------------------------

student1 = "Rahul"
student2 = "Amit"

# INVALID:
#
# 1student = "Rahul"


# ----------------------------------------------------------
# RULE 3: Use underscore _
# ----------------------------------------------------------

first_name = "Shubham"
last_name = "More"
monthly_salary = 70000


# ----------------------------------------------------------
# RULE 4: Spaces are NOT allowed
# ----------------------------------------------------------

# INVALID:
#
# first name = "Shubham"

# CORRECT:

first_name = "Shubham"


# ----------------------------------------------------------
# RULE 5: Avoid special characters
# ----------------------------------------------------------

# INVALID examples:
#
# user@name = "Shubham"
# my-name = "Shubham"
# salary$ = 70000

# CORRECT:

user_name = "Shubham"
monthly_salary = 70000


# ==========================================================
# 9. VARIABLES ARE CASE-SENSITIVE
# ==========================================================

# Python treats lowercase and uppercase
# variable names differently.

name = "Shubham"
Name = "Rahul"
NAME = "Amit"

print(name)
print(Name)
print(NAME)

# These are THREE different variables.


# ==========================================================
# 10. USE MEANINGFUL VARIABLE NAMES
# ==========================================================

# Bad variable name:

x = 70000

# Better variable name:

salary = 70000

# Even more descriptive:

monthly_salary = 70000

print(monthly_salary)

# Meaningful names make code easier to understand.


# ==========================================================
# 11. SNAKE_CASE NAMING CONVENTION
# ==========================================================

# Python commonly uses snake_case for variables.

first_name = "Shubham"
last_name = "More"
monthly_salary = 70000
is_learning_python = True

# Recommended:
#
# monthly_salary
#
# Instead of:
#
# MonthlySalary
# monthlySalary


# ==========================================================
# 12. ASSIGNING MULTIPLE VARIABLES
# ==========================================================

# Normal method:

name = "Shubham"
age = 28
city = "Mumbai"

# Multiple assignment:

name, age, city = "Shubham", 28, "Mumbai"

print(name)
print(age)
print(city)


# ==========================================================
# 13. SAME VALUE TO MULTIPLE VARIABLES
# ==========================================================

a = b = c = 100

print(a)
print(b)
print(c)

# Output:
#
# 100
# 100
# 100


# ==========================================================
# 14. USING VARIABLES IN CALCULATIONS
# ==========================================================

price = 100
quantity = 5

total = price * quantity

print(total)

# Calculation:
#
# price = 100
# quantity = 5
#
# total = 100 * 5
#
# total = 500


# ==========================================================
# 15. REAL-LIFE EXAMPLE - SALARY CALCULATION
# ==========================================================

monthly_salary = 70000
months = 12

annual_salary = monthly_salary * months

print("Monthly Salary:", monthly_salary)
print("Annual Salary:", annual_salary)


# ==========================================================
# 16. USING VARIABLES WITH PRINT()
# ==========================================================

name = "Shubham"
age = 28

print("My name is", name)
print("My age is", age)

# Output:
#
# My name is Shubham
# My age is 28


# ==========================================================
# 17. VARIABLE VS STRING
# ==========================================================

name = "Shubham"

print(name)
print("name")

# Output:
#
# Shubham
# name

# Explanation:
#
# name
# -> Python looks for the variable called name.
#
# "name"
# -> Python treats it as normal text.


# ==========================================================
# 18. F-STRINGS
# ==========================================================

# f-Strings are a clean way to use variables
# inside text.

name = "Shubham"
age = 28

print(f"My name is {name} and I am {age} years old.")

# Python replaces:
#
# {name} -> Shubham
# {age}  -> 28


# ==========================================================
# 19. TAKING INPUT FROM THE USER
# ==========================================================

# Uncomment these lines to test user input.

# name = input("Enter your name: ")
#
# print(name)


# Example with f-string:

# name = input("Enter your name: ")
#
# print(f"Hello {name}, welcome to Python!")


# ==========================================================
# 20. IMPORTANT: input() RETURNS A STRING
# ==========================================================

# Suppose the user enters:
#
# 28
#
# input() stores it as:
#
# "28"
#
# This is a STRING, not an integer.

# age = input("Enter your age: ")
#
# print(age)
# print(type(age))

# Output type:
#
# <class 'str'>


# ==========================================================
# 21. TYPE CONVERSION
# ==========================================================

# We can convert one data type into another.


# String to Integer

age = int("28")

print(age)
print(type(age))


# String to Float

price = float("99.99")

print(price)
print(type(price))


# Integer to String

number = str(100)

print(number)
print(type(number))


# Common conversion functions:
#
# int()
# float()
# str()
# bool()


# ==========================================================
# 22. USER INPUT WITH TYPE CONVERSION
# ==========================================================

# input() gives us a string.
#
# We can convert it using int() or float().

# age = int(input("Enter your age: "))
#
# print(age)
# print(type(age))


# Example flow:
#
# User enters:
#
# 28
#
# input()
#
# "28"
#
# int("28")
#
# 28


# ==========================================================
# 23. VARIABLE TYPE CAN CHANGE
# ==========================================================

value = 100

print(value)
print(type(value))

# Now assign a string

value = "Shubham"

print(value)
print(type(value))

# Python allows the same variable name
# to refer to a different type of value.


# ==========================================================
# 24. NONE
# ==========================================================

# None means there is currently no value.

job_offer = None

print(job_offer)
print(type(job_offer))

# Later we can assign a value:

job_offer = "Data Engineer"

print(job_offer)


# ==========================================================
# 25. VARIABLES WITH LISTS
# ==========================================================

# A variable can also refer to a collection
# of multiple values.

skills = ["Python", "SQL", "Azure"]

print(skills)
print(type(skills))

# Output:
#
# ['Python', 'SQL', 'Azure']


# ==========================================================
# 26. VARIABLES WITH DICTIONARIES
# ==========================================================

employee = {
    "name": "Shubham",
    "age": 28,
    "role": "Data Analyst"
}

print(employee)
print(type(employee))


# ==========================================================
# 27. HOW PYTHON VARIABLES ACTUALLY WORK
# ==========================================================

# For beginners, we often say:
#
# Variable = Box that stores a value
#
# Example:
#
# age = 28
#
# Think:
#
# [ age ] ---> [ 28 ]
#
#
# More accurately:
#
# A Python variable is a NAME that refers
# to an OBJECT in memory.

age = 28

# Conceptually:
#
# age --------> 28
#
# "age" is the variable name.
# 28 is an integer object.


# ==========================================================
# 28. TWO VARIABLES CAN REFER TO THE SAME VALUE
# ==========================================================

a = 100

b = a

print(a)
print(b)

# Conceptually:
#
# a ----\
#        ----> 100
# b ----/


# ==========================================================
# 29. id() FUNCTION
# ==========================================================

# id() gives the identity of an object
# during the current Python program.

a = 100
b = a

print(id(a))
print(id(b))

# In this example, both will typically have
# the same object identity.

# Note:
#
# The actual ID number can change
# between Python runs.


# ==========================================================
# 30. CONSTANTS
# ==========================================================

# Python does not strictly enforce constants.
#
# By convention, constants are written
# using UPPERCASE letters.

PI = 3.14159

MAX_USERS = 100

DATABASE_NAME = "company_db"

print(PI)
print(MAX_USERS)
print(DATABASE_NAME)


# ==========================================================
# 31. = VS ==
# ==========================================================

# = means ASSIGNMENT

age = 28


# == means COMPARISON

print(age == 28)

# Output:
#
# True


# Remember:
#
# =    Assign a value
#
# ==   Compare two values


# ==========================================================
# 32. COMMON BEGINNER MISTAKES
# ==========================================================


# MISTAKE 1:
# Forgetting quotes around text

# WRONG:
#
# name = Shubham

# CORRECT:

name = "Shubham"


# ----------------------------------------------------------


# MISTAKE 2:
# Using spaces in variable names

# WRONG:
#
# first name = "Shubham"

# CORRECT:

first_name = "Shubham"


# ----------------------------------------------------------


# MISTAKE 3:
# Starting variable name with a number

# WRONG:
#
# 1name = "Shubham"

# CORRECT:

name1 = "Shubham"


# ----------------------------------------------------------


# MISTAKE 4:
# Case mismatch

name = "Shubham"

# WRONG:
#
# print(Name)

# CORRECT:

print(name)


# ----------------------------------------------------------


# MISTAKE 5:
# Confusing strings and integers

age_as_text = "28"

age_as_number = 28

print(type(age_as_text))
print(type(age_as_number))

# "28" -> str
#
# 28 -> int


# ==========================================================
# 33. REAL-LIFE EMPLOYEE EXAMPLE
# ==========================================================

employee_name = "Shubham"

employee_age = 28

job_role = "Data Analyst"

monthly_salary = 70000.50

is_employed = True


print("\n--- Employee Details ---")

print(f"Employee Name: {employee_name}")

print(f"Age: {employee_age}")

print(f"Job Role: {job_role}")

print(f"Monthly Salary: {monthly_salary}")

print(f"Currently Employed: {is_employed}")


# ==========================================================
# 34. MINI PROJECT - SALARY CALCULATOR
# ==========================================================

# Uncomment the code below to run the mini project.


# print("\n--- Employee Salary Calculator ---")
#
# employee_name = input(
#     "Enter employee name: "
# )
#
# monthly_salary = float(
#     input("Enter monthly salary: ")
# )
#
# annual_salary = monthly_salary * 12
#
#
# print("\n--- Salary Details ---")
#
# print(
#     f"Employee Name: {employee_name}"
# )
#
# print(
#     f"Monthly Salary: ₹{monthly_salary}"
# )
#
# print(
#     f"Annual Salary: ₹{annual_salary}"
# )


# ==========================================================
# 35. PRACTICE QUESTIONS
# ==========================================================

# Try solving these yourself.


# Question 1:
#
# Create a variable called name
# and store your name.


# Question 2:
#
# Create variables for:
#
# name
# age
# city
# salary
# is_employed


# Question 3:
#
# Print all the above variables.


# Question 4:
#
# Check their data types using type().


# Question 5:
#
# Create:
#
# price = 500
# quantity = 3
#
# Calculate total price.


# Question 6:
#
# Ask the user for their name.
#
# Print:
#
# Hello Shubham, welcome to Python!


# Question 7:
#
# Ask the user for monthly salary.
#
# Calculate annual salary.


# Question 8:
#
# What will be the output?

# x = 10
# x = 20
#
# print(x)

# Answer:
#
# 20
#
# Because x was reassigned.


# ==========================================================
# 36. QUICK REVISION
# ==========================================================

# Variable:
#
# A variable is a name that refers to a value/object.


# String

student_name = "Shubham"


# Integer

student_age = 28


# Float

course_price = 999.99


# Boolean

is_student = True


# None

certificate = None


# Calculation

price = 500

quantity = 2

total = price * quantity


# Print

print(total)


# Type checking

print(type(total))


# f-string

print(
    f"{student_name} is learning Python."
)


# ==========================================================
# FINAL KEY POINT
# ==========================================================

# Remember:
#
# name = "Shubham"
#
# Think:
#
# Variable Name        Value/Object
#
# name  -------------> "Shubham"
#
#
# A Python variable is a name that allows us
# to refer to and work with values/objects
# inside our program.


# ==========================================================
# END OF PYTHON VARIABLES
# ==========================================================
