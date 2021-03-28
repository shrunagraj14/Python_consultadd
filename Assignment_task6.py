# 1. Write a program in Python to find out the character in a string which is uppercase using list
# comprehension.
str_obj = 'Testing UpperCase'
print([elem for elem in str_obj if elem.isupper()])

# 2. Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
# HINT - Use Zip function also
# Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
# Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
dict_z = dict(zip(students, subjects))
print(dict_z)

# 4. Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”
class Generators:
    def rev_str(str_val):
        length = len(str_val)
        reversed_val=str_val[::-1]
        print(reversed_val)
Generators.rev_str("Consultadd Training")

# 5. Write an example on decorators.

def my_decorator(func):
    def inner():
        print("before the function is called.")
        func()
        print("after the function is called.")
    return inner()

@my_decorator
def hello():
    print("Whee!")



