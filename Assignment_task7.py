import math

# #Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.


C = 50
H = 30

val = str(input("Enter the values for D in comma-separated sequence: "))
print("VAL:", val)
D = val.split(",")
print("D:", D)
for i in D:
    print("i:", i)
    Q = math.sqrt((2 * C * int(i)) / H)
    print("Ans:", Q)


# Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument. Both classes have an area function which can print the area of the shape
# where Shape’s area is 0 by default.
class Shape:

    def __init__(self, x, y):
        self.x = 0
        self.y = 0

    def area(self):
        print(self.x * self.y)


class Square(Shape):

    def __init__(self, x):
        self.x = x
        self.y = x

    def area(self):
        print(self.x * self.y)


# Create a class to find three elements that sum to zero from a set of n real numbers
class py_three:
    def sum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result


numbers = [-25, -10, -7, -3, 2, 4, 8, 10]

print(py_three().sum(numbers))


# Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.

class Time:
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def addTime(time1, time2):
        time3 = Time(0, 0)
        time3.hr = time1.hr + time2.hr
        time3.min = time1.min + time2.min
        while time3.min > 60:
            time3.hr += 1
            time3.min -= 60
        return time3

    def displayTime(self):
        print("%d hr and %d min" % (self.hr, self.min))

    def displayMinutes(self):
        print((self.hr * 60) + self.min, "minutes")


a = Time(2, 90)
b = Time(1, 90)
c = Time.addTime(a, b)

c.displayTime()
c.displayMinutes()


# Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:

class Person:
    age = 0

    def __init__(self, ageNumber):
        if ageNumber < 0:
            print("Age is not valid, setting age to 0")
        else:
            self.age = ageNumber

    def amIOld(self):
        if self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age < 18:
            print("You are teenager")
        else:
            print("You are old")

    def yearPasses(self):
        self.age += 1


a = Person(13)
a.amIOld()