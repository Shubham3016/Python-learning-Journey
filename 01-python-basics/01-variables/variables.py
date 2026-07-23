

### `variables.py` = Actual runnable code

Don't put your entire textbook inside Python comments.

Keep actual examples here:

```python
# =========================================
# Python Variables
# =========================================

# String variable
name = "Shubham"

# Integer variable
age = 28

# Float variable
salary = 70000.50

# Boolean variable
is_learning_python = True

print(name)
print(age)
print(salary)
print(is_learning_python)


# Checking data types

print(type(name))
print(type(age))
print(type(salary))
print(type(is_learning_python))


# Variable reassignment

age = 27
print(age)

age = 28
print(age)


# Multiple assignment

name, age, city = "Shubham", 28, "Mumbai"

print(name)
print(age)
print(city)
