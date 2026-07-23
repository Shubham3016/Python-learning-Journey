
# 🐍 Python Variables — Complete Beginner Guide

> A simple, step-by-step guide to understanding **variables in Python**, written for absolute beginners.

---

## 📚 Table of Contents

1. [What is a Variable?](#1-what-is-a-variable)
2. [Creating Your First Variable](#2-creating-your-first-variable)
3. [Why Do We Need Variables?](#3-why-do-we-need-variables)
4. [How Variables Work](#4-how-variables-work)
5. [Different Data Types](#5-different-data-types)
6. [Checking Data Types](#6-checking-data-types)
7. [Variables Can Change](#7-variables-can-change)
8. [Variable Naming Rules](#8-variable-naming-rules)
9. [Case Sensitivity](#9-case-sensitivity)
10. [Good Variable Names](#10-good-variable-names)
11. [Snake Case](#11-snake-case)
12. [Multiple Variable Assignment](#12-multiple-variable-assignment)
13. [Variables in Calculations](#13-variables-in-calculations)
14. [Variables with `print()`](#14-variables-with-print)
15. [f-Strings](#15-f-strings)
16. [Taking User Input](#16-taking-user-input)
17. [Type Conversion](#17-type-conversion)
18. [`None`](#18-none)
19. [How Python Variables Actually Work](#19-how-python-variables-actually-work)
20. [Constants](#20-constants)
21. [`=` vs `==`](#21--vs-)
22. [Common Beginner Mistakes](#22-common-beginner-mistakes)
23. [Real-Life Example](#23-real-life-example)
24. [Mini Project](#24-mini-project)
25. [Practice Questions](#25-practice-questions)
26. [Interview Questions](#26-interview-questions)
27. [Quick Cheat Sheet](#27-quick-cheat-sheet)

---

# 1. What is a Variable?

Imagine you have some **boxes**.

You put different things inside those boxes:

- 📦 One box contains your **name**
- 📦 One box contains your **age**
- 📦 One box contains your **salary**
- 📦 One box contains your **city**

To identify each box, you put a **label** on it.

For example:

```text
┌─────────────────┐
│    "Shubham"    │
└─────────────────┘
       name


┌─────────────────┐
│       28        │
└─────────────────┘
       age
```

In programming, we can think of these labeled boxes as **variables**.

In Python:

```python
name = "Shubham"
age = 28
```

A simple way to think about it:

```text
Variable Name          Value

    name    ────────► "Shubham"

    age     ────────► 28
```

### Simple Definition

> **A variable is a name that allows us to refer to and work with a value in our program.**

---

# 2. Creating Your First Variable

Creating a variable in Python is very simple.

```python
name = "Shubham"
```

Let's break it down:

```text
name      =      "Shubham"

 ↓        ↓          ↓

Variable  Assignment  Value
Name      Operator
```

The `=` symbol is called the **assignment operator**.

It means:

> Take the value on the right and assign it to the variable name on the left.

Example:

```python
age = 28
```

This means:

```text
age ─────────► 28
```

Another example:

```python
city = "Mumbai"
```

This means:

```text
city ─────────► "Mumbai"
```

---

# 3. Why Do We Need Variables?

Imagine writing:

```python
print("Shubham")
print("Shubham")
print("Shubham")
print("Shubham")
```

Instead of repeating `"Shubham"`, we can store it in a variable.

```python
name = "Shubham"

print(name)
print(name)
print(name)
print(name)
```

Output:

```text
Shubham
Shubham
Shubham
Shubham
```

Now suppose we want to change the name.

We only change:

```python
name = "Rahul"
```

Now every place that uses `name` gets the new value.

Variables help us:

- Store information
- Reuse information
- Change values easily
- Perform calculations
- Make programs easier to understand
- Avoid repeating the same data

---

# 4. How Variables Work

Consider:

```python
name = "Shubham"
age = 28
salary = 70000
```

For now, imagine:

```text
┌──────────┐        ┌─────────────┐
│   name   │ ─────► │  "Shubham"  │
└──────────┘        └─────────────┘

┌──────────┐        ┌─────────────┐
│   age    │ ─────► │     28      │
└──────────┘        └─────────────┘

┌──────────┐        ┌─────────────┐
│  salary  │ ─────► │    70000    │
└──────────┘        └─────────────┘
```

For beginners:

> Think of a variable as a **labeled box containing information**.

Later, we will learn that technically Python variables are **names that reference objects**.

---

# 5. Different Data Types

Variables can refer to different types of data.

The most common beginner data types are:

| Data Type | Meaning | Example |
|---|---|---|
| `str` | Text | `"Shubham"` |
| `int` | Whole Number | `28` |
| `float` | Decimal Number | `5.8` |
| `bool` | True or False | `True` |
| `NoneType` | No value | `None` |

Let's understand each one.

---

## 5.1 String — `str`

Strings are used to store **text**.

```python
name = "Shubham"
city = "Mumbai"
job_role = "Data Analyst"
```

Strings are normally written inside quotes.

```python
"Hello"
```

or:

```python
'Hello'
```

Examples:

```python
first_name = "Shubham"

company = "ABC Technologies"

country = "India"
```

---

## 5.2 Integer — `int`

Integers are **whole numbers**.

Examples:

```python
age = 28

salary = 70000

year = 2026
```

These are integers:

```text
10
25
100
5000
-20
```

These are not integers:

```text
10.5
99.99
```

Those are floats.

---

## 5.3 Float — `float`

Floats are numbers containing a **decimal point**.

```python
height = 5.8

price = 99.99

temperature = 36.5
```

Examples:

```text
5.5
10.25
99.99
-3.14
```

---

## 5.4 Boolean — `bool`

A Boolean has only two possible values:

```python
True

False
```

Example:

```python
is_learning_python = True

is_employed = True

is_married = False
```

Think of Boolean values as answering a **Yes/No question**.

```text
Is the user employed?

Yes → True
No  → False
```

### Important

Correct:

```python
True
False
```

Incorrect:

```python
true
false
```

Python is case-sensitive.

---

# 6. Checking Data Types

Python provides the `type()` function.

It tells us the type of a value.

Example:

```python
name = "Shubham"
age = 28
height = 5.8
is_employee = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_employee))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Think of `type()` as asking Python:

> "Python, what kind of data is this?"

---

## Python Automatically Detects the Type

We don't normally have to explicitly tell Python:

```text
This is a String.

This is an Integer.

This is a Float.
```

We simply write:

```python
name = "Shubham"

age = 28

salary = 70000.50
```

Python understands:

```text
"Shubham"   → str

28          → int

70000.50    → float
```

Python is a **dynamically typed language**.

---

# 7. Variables Can Change

The value associated with a variable name can change.

Example:

```python
age = 27

print(age)
```

Output:

```text
27
```

Now change it:

```python
age = 28

print(age)
```

Output:

```text
28
```

Complete example:

```python
age = 27

print(age)

age = 28

print(age)
```

Output:

```text
27
28
```

This is called **reassignment**.

Conceptually:

```text
BEFORE

age ─────────► 27


AFTER

age ─────────► 28
```

The latest assigned value is used.

---

# 8. Variable Naming Rules

Python has some rules for naming variables.

---

## Rule 1: Use Letters

Valid:

```python
name = "Shubham"

age = 28

salary = 70000
```

---

## Rule 2: Numbers Are Allowed

Valid:

```python
student1 = "Rahul"

student2 = "Amit"
```

But a variable **cannot start with a number**.

❌ Wrong:

```python
1student = "Rahul"
```

✅ Correct:

```python
student1 = "Rahul"
```

---

## Rule 3: Use Underscores

Valid:

```python
first_name = "Shubham"

last_name = "More"

monthly_salary = 70000
```

The underscore `_` helps separate words.

---

## Rule 4: Spaces Are Not Allowed

❌ Wrong:

```python
first name = "Shubham"
```

✅ Correct:

```python
first_name = "Shubham"
```

---

## Rule 5: Avoid Special Characters

❌ Invalid:

```python
user@name = "Shubham"

my-name = "Shubham"

salary$ = 70000
```

✅ Correct:

```python
user_name = "Shubham"

monthly_salary = 70000
```

---

## Quick Naming Table

| Variable | Valid? |
|---|---|
| `name` | ✅ |
| `first_name` | ✅ |
| `student1` | ✅ |
| `_name` | ✅ |
| `1student` | ❌ |
| `first name` | ❌ |
| `user-name` | ❌ |
| `user@name` | ❌ |

---

# 9. Case Sensitivity

Python variable names are **case-sensitive**.

Consider:

```python
name = "Shubham"

Name = "Rahul"

NAME = "Amit"
```

These are three different variables:

```text
name ≠ Name ≠ NAME
```

Example:

```python
print(name)
print(Name)
print(NAME)
```

Output:

```text
Shubham
Rahul
Amit
```

For normal variables, it is usually best to use lowercase names.

---

# 10. Good Variable Names

Technically, you can write:

```python
x = 70000
```

But what does `x` mean?

It is difficult to understand.

Better:

```python
salary = 70000
```

Even more descriptive:

```python
monthly_salary = 70000
```

Compare:

❌ Poor naming:

```python
a = "Shubham"
b = 28
c = 70000
```

✅ Better naming:

```python
employee_name = "Shubham"

employee_age = 28

monthly_salary = 70000
```

### Rule to Remember

> A good variable name should explain what the value represents.

---

# 11. Snake Case

Python commonly uses **snake_case** for variable names.

Example:

```python
first_name = "Shubham"

last_name = "More"

monthly_salary = 70000

is_learning_python = True
```

Preferred:

```python
monthly_salary
```

Instead of:

```python
MonthlySalary
```

or:

```python
monthlySalary
```

Use meaningful **snake_case** variable names.

---

# 12. Multiple Variable Assignment

Normally, we write:

```python
name = "Shubham"

age = 28

city = "Mumbai"
```

Python also allows:

```python
name, age, city = "Shubham", 28, "Mumbai"
```

Now:

```python
print(name)
print(age)
print(city)
```

Output:

```text
Shubham
28
Mumbai
```

Conceptually:

```text
name ─────────► "Shubham"

age  ─────────► 28

city ─────────► "Mumbai"
```

For beginners, separate lines are often easier to read.

---

## Same Value to Multiple Variables

Python also allows:

```python
a = b = c = 100
```

Now:

```python
print(a)
print(b)
print(c)
```

Output:

```text
100
100
100
```

Conceptually:

```text
a ───┐
     │
b ───┼──────► 100
     │
c ───┘
```

---

# 13. Variables in Calculations

Variables are extremely useful for calculations.

Example:

```python
price = 100

quantity = 5

total = price * quantity

print(total)
```

Output:

```text
500
```

Step-by-step:

```text
price = 100

quantity = 5

        ↓

total = price × quantity

        ↓

total = 100 × 5

        ↓

total = 500
```

---

## Real-Life Salary Example

```python
monthly_salary = 70000

months = 12

annual_salary = monthly_salary * months

print(annual_salary)
```

Output:

```text
840000
```

Flow:

```text
monthly_salary ───► 70000

months ───────────► 12

        70000 × 12

             ↓

          840000

             ↓

      annual_salary
```

---

# 14. Variables with `print()`

Python uses `print()` to display information.

Example:

```python
name = "Shubham"

age = 28

print(name)

print(age)
```

Output:

```text
Shubham
28
```

You can combine text and variables:

```python
print("My name is", name)

print("My age is", age)
```

Output:

```text
My name is Shubham
My age is 28
```

---

## Variable vs String

This is very important.

```python
name = "Shubham"

print(name)

print("name")
```

Output:

```text
Shubham
name
```

Why?

### `name`

```python
print(name)
```

means:

> Python, find the variable called `name` and print its value.

### `"name"`

```python
print("name")
```

means:

> Print the actual text `name`.

So:

```text
name       → Variable

"name"     → String/Text
```

---

# 15. f-Strings

f-Strings are a clean and modern way to use variables inside text.

Example:

```python
name = "Shubham"

age = 28

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Shubham and I am 28 years old.
```

How does it work?

```python
f"My name is {name}"
```

The `f` tells Python that variables or expressions may appear inside `{}`.

Python replaces:

```text
{name} → Shubham

{age}  → 28
```

Another example:

```python
product = "Laptop"

price = 50000

print(f"The price of {product} is ₹{price}")
```

Output:

```text
The price of Laptop is ₹50000
```

---

# 16. Taking User Input

Python provides the `input()` function.

Example:

```python
name = input("Enter your name: ")

print(name)
```

Suppose the user enters:

```text
Shubham
```

Then:

```text
name ─────────► "Shubham"
```

We can use it with an f-string:

```python
name = input("Enter your name: ")

print(f"Hello {name}, welcome to Python!")
```

Example output:

```text
Enter your name: Shubham

Hello Shubham, welcome to Python!
```

---

## Important: `input()` Returns a String

Consider:

```python
age = input("Enter your age: ")
```

Suppose the user enters:

```text
28
```

You might think Python stores:

```python
28
```

But `input()` actually returns:

```python
"28"
```

That means it is a string.

Check:

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

This leads us to **type conversion**.

---

# 17. Type Conversion

Type conversion means changing one data type into another.

Common functions are:

```python
int()

float()

str()

bool()
```

---

## String to Integer

```python
age = int("28")

print(age)

print(type(age))
```

Now `age` is an integer.

```text
"28"

 ↓ int()

28
```

---

## String to Float

```python
price = float("99.99")

print(price)

print(type(price))
```

Conversion:

```text
"99.99"

   ↓ float()

99.99
```

---

## Integer to String

```python
number = str(100)

print(number)

print(type(number))
```

Conversion:

```text
100

 ↓ str()

"100"
```

---

## User Input with Type Conversion

Suppose we need the user's age as a number:

```python
age = int(input("Enter your age: "))
```

Step-by-step:

```text
User enters:

28

      ↓

input()

      ↓

"28"

      ↓

int("28")

      ↓

28
```

Now `age` is an integer.

---

# 18. `None`

Sometimes we don't have a value yet.

Python provides:

```python
None
```

Example:

```python
job_offer = None
```

Think of it as:

```text
job_offer

    ↓

No value yet
```

Later:

```python
job_offer = "Data Engineer"
```

Now:

```text
job_offer ─────► "Data Engineer"
```

`None` is useful when:

- Data is missing
- A result is not available yet
- A value will be assigned later

---

# 19. How Python Variables Actually Work

Until now, we used the **box analogy**:

```text
Variable = Labeled Box
```

This is useful for beginners.

But technically, Python variables are better understood as **names that refer to objects**.

Consider:

```python
age = 28
```

A more accurate mental model is:

```text
Variable Name             Object

┌────────────┐          ┌────────────┐
│    age     │ ───────► │     28     │
└────────────┘          └────────────┘
```

So:

- `age` is the variable name
- `28` is an integer object/value
- `age` refers to that object

### Simple Version

> Variable = Box

### More Accurate Python Version

> Variable = Name/Reference to an object

This concept becomes important later when learning:

- Lists
- Mutable vs immutable objects
- Functions
- Object-Oriented Programming
- Memory management

---

## Two Variables Can Refer to the Same Object

Example:

```python
a = 100

b = a
```

Conceptually:

```text
a ──────┐
        │
        ├──────► 100
        │
b ──────┘
```

Now:

```python
print(a)

print(b)
```

Output:

```text
100
100
```

---

## The `id()` Function

Python provides:

```python
id()
```

It gives the identity of an object during the current Python process.

Example:

```python
a = 100

b = a

print(id(a))

print(id(b))
```

Both names typically refer to the same object here.

> Do not memorize the actual ID number. It can differ between Python runs.

This is an advanced concept. For now, focus mainly on variables, values, assignment, and data types.

---

# 20. Constants

Sometimes we have values that should conceptually remain unchanged.

Example:

```python
PI = 3.14159
```

Python does not strictly enforce constants like some other programming languages.

Instead, Python programmers use **UPPERCASE names as a convention**.

Example:

```python
PI = 3.14159

MAX_USERS = 100

DATABASE_NAME = "company_db"
```

When you see:

```python
MAX_USERS
```

it tells programmers:

> This value is intended to be treated as a constant.

---

# 21. `=` vs `==`

This is one of the most important beginner concepts.

## `=` Assignment Operator

```python
age = 28
```

Meaning:

> Assign `28` to `age`.

---

## `==` Comparison Operator

```python
age == 28
```

Meaning:

> Is the value of `age` equal to `28`?

Example:

```python
age = 28

print(age == 28)
```

Output:

```text
True
```

Remember:

```text
=      Assignment

==     Comparison
```

---

# 22. Common Beginner Mistakes

## Mistake 1: Forgetting Quotes

❌ Wrong:

```python
name = Shubham
```

Python thinks `Shubham` is another variable name.

✅ Correct:

```python
name = "Shubham"
```

---

## Mistake 2: Using Spaces

❌ Wrong:

```python
first name = "Shubham"
```

✅ Correct:

```python
first_name = "Shubham"
```

---

## Mistake 3: Starting with a Number

❌ Wrong:

```python
1name = "Shubham"
```

✅ Correct:

```python
name1 = "Shubham"
```

---

## Mistake 4: Case Mismatch

```python
name = "Shubham"

print(Name)
```

This causes an error because:

```text
name ≠ Name
```

Correct:

```python
print(name)
```

---

## Mistake 5: Confusing Strings and Numbers

```python
age = "28"
```

This is a:

```text
String → str
```

But:

```python
age = 28
```

This is an:

```text
Integer → int
```

They are different data types.

---

# 23. Real-Life Example

Let's create a simple employee profile.

```python
employee_name = "Shubham"

employee_age = 28

job_role = "Data Analyst"

monthly_salary = 70000.50

is_employed = True
```

Now display the information:

```python
print(f"Employee Name: {employee_name}")

print(f"Age: {employee_age}")

print(f"Job Role: {job_role}")

print(f"Monthly Salary: ₹{monthly_salary}")

print(f"Currently Employed: {is_employed}")
```

Output:

```text
Employee Name: Shubham
Age: 28
Job Role: Data Analyst
Monthly Salary: ₹70000.5
Currently Employed: True
```

We used several data types:

```text
employee_name       → str

employee_age        → int

job_role            → str

monthly_salary      → float

is_employed         → bool
```

---

# 24. Mini Project

## 💼 Employee Salary Calculator

Let's create a small project using everything we learned.

### Goal

The program should:

1. Ask for employee name
2. Ask for monthly salary
3. Calculate annual salary
4. Display the result

### Code

```python
print("===== Employee Salary Calculator =====")

employee_name = input(
    "Enter employee name: "
)

monthly_salary = float(
    input("Enter monthly salary: ")
)

annual_salary = monthly_salary * 12

print("\n===== Salary Details =====")

print(
    f"Employee Name: {employee_name}"
)

print(
    f"Monthly Salary: ₹{monthly_salary}"
)

print(
    f"Annual Salary: ₹{annual_salary}"
)
```

Example:

```text
===== Employee Salary Calculator =====

Enter employee name: Shubham

Enter monthly salary: 70000


===== Salary Details =====

Employee Name: Shubham

Monthly Salary: ₹70000.0

Annual Salary: ₹840000.0
```

---

## What Did We Learn from This Project?

```text
User Input
    ↓
Variables
    ↓
Data Types
    ↓
Type Conversion
    ↓
Calculation
    ↓
f-Strings
    ↓
Output
```

This small project combines multiple Python basics into one program.

---

# 25. Practice Questions

Try solving these yourself.

Do not immediately look for the answer.

---

### Question 1

Create a variable called `name` and store your name.

---

### Question 2

Create variables for:

```text
name
age
city
salary
is_employed
```

Use the correct data types.

---

### Question 3

Print all the variables from Question 2.

---

### Question 4

Check the data type of every variable using:

```python
type()
```

---

### Question 5

Create:

```python
price = 500

quantity = 3
```

Calculate:

```text
total_price
```

Expected result:

```text
1500
```

---

### Question 6

Ask the user for their name.

Print:

```text
Hello Shubham, welcome to Python!
```

Use an f-string.

---

### Question 7

Ask the user for their monthly salary.

Calculate their annual salary.

Formula:

```text
Annual Salary = Monthly Salary × 12
```

---

### Question 8

What will be the output?

```python
x = 10

x = 20

print(x)
```

Think before checking.

<details>
<summary>Click to see answer</summary>

```text
20
```

Why?

Because `x` was reassigned from `10` to `20`.

</details>

---

### Question 9

What is wrong with this code?

```python
first name = Shubham

age = "28"

print(Name)
```

Try finding all the problems.

---

### Question 10

Create variables for a product:

```text
product_name
product_price
quantity
is_available
```

Calculate the total cost.

---

# 26. Interview Questions

## Q1. What is a variable in Python?

A variable is a **name that refers to a value/object**.

Example:

```python
age = 28
```

Here:

```text
age → Variable Name

28  → Value/Object
```

---

## Q2. Do we need to declare variable types in Python?

No.

Python automatically determines the data type.

Example:

```python
name = "Shubham"

age = 28
```

Python understands:

```text
name → str

age  → int
```

---

## Q3. Is Python dynamically typed?

Yes.

Example:

```python
value = 100

value = "Hello"
```

The same variable name can later refer to a value of a different type.

---

## Q4. Are Python variables case-sensitive?

Yes.

```text
name

Name

NAME
```

are different variable names.

---

## Q5. What is the difference between `=` and `==`?

```text
=      Assignment

==     Comparison
```

Example:

```python
age = 28

age == 28
```

---

## Q6. What does `None` mean?

`None` represents the absence of a value.

Example:

```python
result = None
```

---

## Q7. What naming convention is commonly used for Python variables?

Python commonly uses:

```text
snake_case
```

Example:

```python
first_name = "Shubham"

monthly_salary = 70000
```

---

# 27. Quick Cheat Sheet

```python
# ========================================
# PYTHON VARIABLES - QUICK CHEAT SHEET
# ========================================


# String

name = "Shubham"


# Integer

age = 28


# Float

salary = 70000.50


# Boolean

is_employee = True


# No value

job_offer = None


# Print variable

print(name)


# Check data type

print(type(name))


# Multiple assignment

name, age = "Shubham", 28


# Same value to multiple variables

a = b = c = 100


# User input

city = input("Enter your city: ")


# Convert input to integer

age = int(
    input("Enter your age: ")
)


# Convert input to float

salary = float(
    input("Enter salary: ")
)


# Calculation

monthly_salary = 70000

annual_salary = monthly_salary * 12


# f-String

print(
    f"My name is {name}"
)


# Reassignment

age = 28

age = 29


# Constant convention

PI = 3.14159
```

---

# 🧠 Final Mental Model

Whenever you see:

```python
name = "Shubham"
```

Think:

```text
Variable Name              Value/Object

┌──────────────┐         ┌──────────────┐
│     name     │ ──────► │  "Shubham"   │
└──────────────┘         └──────────────┘
```

When Python sees:

```python
print(name)
```

Think:

```text
print(name)

     ↓

Find what "name" refers to

     ↓

"Shubham"

     ↓

Display the value

     ↓

Shubham
```

---

# ⭐ Key Takeaway

> **A Python variable is a name that allows us to refer to and work with a value/object inside our program.**

Remember these five things:

```text
1. Create a variable
        ↓
   name = "Shubham"

2. Use meaningful names
        ↓
   monthly_salary = 70000

3. Understand data types
        ↓
   str, int, float, bool

4. Variables can be reassigned
        ↓
   age = 27
   age = 28

5. Use variables to build programs
        ↓
   Input → Process → Output
```

---

## 📂 Files in This Topic

```text
01_variables/
│
├── README.md
│   └── Complete notes and explanation
│
├── variables.py
│   └── Python variable examples
│
├── practice.py
│   └── Practice problems
│
└── salary_calculator.py
    └── Mini project
```

---

## 🚀 What's Next?

After learning variables, continue with:

```text
Variables
    ↓
Data Types
    ↓
Type Conversion
    ↓
Input & Output
    ↓
Operators
    ↓
Strings
    ↓
Conditional Statements
    ↓
Loops
    ↓
Lists / Tuples / Sets / Dictionaries
    ↓
Functions
    ↓
Object-Oriented Programming
```

---

### Happy Coding! 🐍💻

**Keep learning. Keep practicing. Keep building.**
