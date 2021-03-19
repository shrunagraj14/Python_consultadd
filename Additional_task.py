# 1 Access List

x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]

# AccessList: [1,2,3,4]
print(x[5][0:4])

# AccessList: [600,700]
print(x[6:8])

# AccessList: [100,300,500,600,800]
print(x[::2])

# AccessList: reverse
print(x[::-1])

# AccessList : [10]
print(x[5][5][0:1])

# AccessList []
x.clear()
print(x)

##2 Create a list of 1000 numbers using range and xrange and understnad the difference

rangeList = []

for i in range(0, 1000, 1):
    rangeList.append(i)
print(rangeList)

##Python 2
# xrangeList = []
# for i in xrange(0,1000,1):
#     xrangeList.append(i)
# print(xrangeList)

### 3 How Tuple is beneficial compared to list
##Ans: tuples can be used as key in dictionary as these are immutable but list can't be used because list is mutable.
### Also tuples can store multiple data type elements but lists cannot store different types.

####4 : Iterate through a list and display number which is divisible by 3 and multiple of 2

for i in range(1, 100, 1):
    if i % 2 == 0 and i % 3 == 0:
        print('Multiple of 2 and divisible by 3:', i)

#### 5. reverse string and print vowel if it exist

str = "testi"
print("Reverse of str:", str[::-1])
vowels = ['a', 'e', 'i', 'o', 'u']
for x in vowels:
    if x in str.lower():
        print(x)

#### 6. print even length words in a string

str = "hello my name is abcde"

str = str.split(" ")
for wrd in str:
    if len(wrd) % 2 == 0:
        print(wrd)

### 7. Program to calculate the sum equals to 8 with pair
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
sum = 8
x.sort()

(lower, higher) = (0, len(x) - 1)

while lower < higher:
    if x[lower] + x[higher] == sum:
        print((x[lower], x[higher]))

    if x[lower] + x[higher] < sum:
        lower = lower + 1
    else:
        higher = higher - 1

#### 8. Create even and odd list add 5 numbers based on input and print sum

evenList = []
oddList = []
evenCount = 0
oddCount = 0
evensum = 0
oddsum = 0

while evenCount < 5 or oddCount < 5:
    number = int(input("Enter a number between 1 to 50:"))
    if number > 50 or number < 1:
        number = int(input("Not a valid number! Please enter a valid number between 1 to 50:"))
    else:
        if number % 2 == 0:
            evenList.append(number)
            evenCount = evenCount + 1
        else:
            oddList.append(number)
            oddCount = oddCount + 1
print(evenList)
print(oddList)
for k in range(0, len(evenList)):
    evensum = evensum + evenList[k]
for l in range(0, len(oddList)):
    oddsum = oddsum + oddList[l]
print("EvenSum:", evensum, "OddSum:", oddsum)

#### 9. Occuurance of each character in a string
input = '12abcbacbaba344ab'

freq = {}
for i in input:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

# 10. create even tuple

sam_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list_tuple = []

for i in sam_tuple:
    if i % 2 == 0:
        list_tuple.append(i)
result_tuple = tuple(list_tuple)
print(result_tuple)















