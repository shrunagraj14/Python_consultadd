# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError
# try:
#     while True:
#         print("Hello")
# except SyntaxError as error:
#     Logging.log_exception(error)

# 2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.
from sys import argv

prog_name, file_name = argv

while True:
    try:
        file_opened = open(file_name)
        value = file_opened.read()
        print(value)
        file_opened.close()
        break
    except:
        file_name = input("Incorrect file name entered, enter the correct name")

# 3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”

number = int(input("Enter a number: "))
try:
    if len(str(number)) > 4 or len(str(number)) < 4:
        raise Exception("The length is too short/long !!! Please provide only four digits")
    else:
        print("Entered Number:", number)
except Exception as e:
    print(e)

# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but
# it should not be more than 3 times.


user_name = input("Username: ")
password = input("Password: ")
count = 0
while count < 2:
    if user_name == "abcxyz" and password == "abcpass":
        print("Successfull Login!!")
    else:
        user_name = input("Username: ")
        password = input("Password: ")
        count += 1

# 5. Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
file_obj = open("doc.txt", 'r')
value = file_obj.read()
for i in value.split():
    if len(i) % 2 == 0:
        print(i)
file_obj.close()