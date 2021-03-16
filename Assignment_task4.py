# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”

str = "1234abcd"
rev_str = str[::-1]
print( rev_str)


# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

new_str ="abcSdefPghijQkl"

upper_case = 0
lower_case = 0

for x in new_str:
    if x.isupper():
        upper_case += 1
    else:
        lower_case += 1

print("Upper case letters:", upper_case)
print("Lower case letters:", lower_case)



# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

list1 = [1, 3, 3, 4, 9, 2, 9, 7, 1]
new_list = set(list1)
print(list(new_list))



# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

str = "life-is-beautiful"

new_str = str.split("-")
print(sorted(new_str))

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

str = input("Enter new string: ")
new_string = str.upper()
print(new_string)



# 6. Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.

def suminteger(a,b):
    add = int(a)+ int(b)
    return add

print(suminteger(4,7))

# 7. Define a function that can accept two strings as input and print the string with the maximum length in the console. If two strings have the same length,
# then the function should print both the strings line by line.

def maxString(str1,str2):
    if len(str1) == len(str2):
        return str1, str2
    elif len(str1) > len(str2):
        return str1
    else:
        return str2


print(maxString('plants','tree'))
print(maxString('book','tree'))
print(maxString('python','consultadd'))


# 8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).

def seq():
    new_list = []
    for x in range(1,21):
        x =x**2
        new_list.append(x)
    return tuple(new_list)

print(seq())

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def showNumbers(limit):
    x = int(limit)
    for i in range(0,x+1):
        if i%2==0:
            print("Even :",i)
        else:
            print("Odd :", i)

print(showNumbers(5))




# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)

m = range(1,21)
var = list(filter(lambda x:x%2==0, m))
print(var)

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.

x = [1,2,3,4,5,6,7,8,9,10]
var = list(map(lambda y:y*y, filter(lambda y:y%2==0, x)))
print(var)

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions

def divExp(x, y):
    try:
        result = x/y
        return result
    except ZeroDivisionError:
        print("Division by zero")

print(divExp(5,0))


# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

from functools import reduce

l =[1,2,3,4,5,6,7]

var = reduce(lambda x, y:10*x+y, l)
print(var)


# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.

l = int(input ("Enter the number:"))

var = list(filter(lambda x : x%3!=0 and x%7==0, range(l)))
print(var)



# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.

def mulSequence(num):
    result = list(map(lambda x: x * x, num))
    return result

numbers = (1, 2, 3, 4)
result = mulSequence(numbers)
print(result)



# 16. What is the output of the following codes:
"""
(i) 
def foo():
  try:
      return 1
  finally:
      return 2
k = foo()
print(k)"""

# output is 2


"""(ii) 
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()
"""

#NameError: name 'f' is not defined
