""" 1. Create three variables in a single line and assign values to them in such a manner that each one of
them belongs to a different data type"""
from platform import python_version

from pip._vendor.distlib.compat import raw_input

a, b, c = 1, 2.01, 'string'
print(type(a), type(b), type(c))

# 2. Create a variable of type complex and swap it with another variable of type integer.
p = 1 + 2j
q = 25
p, q = q, p
print(p)
print(q)

# 3. Swap two numbers using a third variable and do the same task without using any third variable.
x = 6
y = 7

temp = x
x = y
y = temp

print(x)
print(y)

# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

name = input("Enter your name: ")
print(name, python_version())

name = raw_input("Enter your name: ")
print(name)

""" 5. Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output."""

num1, num2 = input("Enter any two numbers between 1 to 10: ").split(" ")
z = int(num1) + int(num2)
result = 30 + z
print("Final output:", result)

""" 6. Write a program to check the data type of the entered values.
HINT: Printed output should say - The data type of the input value is : int/float/string/etc """

x = input("Enter any variable: ")
print(type(x))

""" 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCASE.
(Refer: https://capitalizemytitle.com/camel-case/)"""

# Upper CamelCase
NewVariable = 5

# Lower camelcase
newVariable = 7

# snake case
new_variable = 9

"""8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ 
again. Will it change the value? If Yes then Why? """

a = 5
print(a)

a = "string"
print(a)

# Yes, because python is dynamically typed language.
