""" 1. Write a program in Python to perform the following operation:
- If a number is divisible by 3 it should print “Consultadd” as a string
- If a number is divisible by 5 it should print “Python Training” as a string
- If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string"""

num = int(input("Enter any number: "))
if (num%3 ==0) and (num % 5 ==0):
    print("Consultadd - Python Training")
elif (num % 5==0):
    print("Python Training")
elif (num % 3 == 0):
    print("Consultadd")
else:
    print(" ")


""" 2. Write a program in Python to perform the following operator based task:
- Ask user to choose the following option first:
  If User Enter 1 - Addition
  If User Enter 2 - Subtraction
  If User Enter 3 - Division
  If User Enter 4 - Multiplication
  If User Enter 5 - Average
- Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
- Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
- At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
x = int(input("Enter any number between 1 to 5: "))
if x==1:
    result = num1+ num2
elif x==2:
    result = num1- num2
elif x==3:
    result = num1/num2
elif x==4:
    result = num1*num2
elif x==5:
    result = (num1 + num2)/2

print("Result",result)
if result<0:
    print("Negative")


#3. Write a program in Python to implement the given flowchart:
a,b,c = 10, 20, 30
avg = (a+b+c)/3
print ("Average= ", avg)

if avg>a and avg>b and avg>c:
    print("Average is higher than a, b,c")
elif avg>a and avg>b:
    print("Average is higher than a, b")
elif avg>a and avg>c:
    print("Average is higher than a, c")
elif avg>b and avg>c:
    print("Average is higher than b, c")
elif avg>a :
    print("Average is higher than a")
elif avg>b :
    print("Average is higher than b")
elif avg>c :
    print("Average is higher than c")



""" 4. Write a program in Python to break and continue if the following cases occurs:
- If user enters a negative number just break the loop and print “It’s Over”
- If user enters a positive number just continue in the loop and print “Good Going”
"""
while True:
    num = int(input("Enter any number: "))
    if num<0:
        print("Its Over")
        break
    elif num>0:
        print("Good going")
        continue



""" 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200.
"""

out = []
for i in range(2000,3200):
    if i % 7== 0 and  i %5 !=0 :
        out.append(i)
print(out)



#6. What is the output of the following code examples?
#
# x=123
# for i in x:
#     print(i)

# TypeError: 'int' object is not iterable


# i=0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
#     else:
#         print("error")

'''
0
error
1
error
2
'''


# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         Break

# NameError: name 'Break' is not defined


"""7. Write a program that prints all the numbers from 0 to 6 except 3 and 6. 
Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement """

new_list =[]
for i in range(0,7):
    if i==6:
        continue
    elif i==3:
        continue
    else:
        new_list.append(i)
print(new_list)


"""8. Write a program that accepts a string as an input from the user and calculate the number of digits
and letters. 
Sample input: consul72 
Expected output: Letters 6 Digits 2 """

new_str = input("Enter any string:")
letters = 0
digits = 0
for i in new_str:
    if (i.isdigit()):
        digits += 1
    else:
        letters += 1
print("Letters: ",letters)
print("Digits: ",digits)

"""9. Read the two parts of the question below:
- Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.
- Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number)"""

lucky_num = 4

while True:
    number = int(input("Guess the lucky number: "))
    if number == lucky_num:
        print ("You guessed the correct number")
        break
    else:
        print ("Try guessing again")




"""10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as
- counter=1
  While counter <= 5:
  print(“Type in the”, counter, “number”
  counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”
"""

lucky_num = 4
counter =1
guess = False
while counter<=5:
    number = int(input("Guess the lucky number: "))
    counter = counter + 1
    print(number)
    if number == lucky_num:
        print ("Good guess")
        guess = True
    elif counter<=5:
        print ("Try again")
if not guess:
    print("Game is over")



""" 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”. """

lucky_num = 4
counter =1
guess = False
while counter<=5:
    number = int(input("Guess the lucky number: "))
    counter = counter + 1
    print(number)
    if number == lucky_num:
        print ("Good guess")
        guess = True
        break
    elif counter<=5:
        print ("Try again")
if not guess:
    print("Game is over")
print("Sorry but that was not very successful")