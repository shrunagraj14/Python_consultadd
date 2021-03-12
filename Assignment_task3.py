# 1. Create a list of 10 elements of four different data types like int, string, complex and float.

list1 = [1,2,3,'six','str', 2j, 3-6j, -7j, 0.768, 34.89]
print(list1)

# 2. Create a list of size 5 and execute the slicing structure
list2 = [20, 30, 40, 50 , 60]
print(list2[1:2])
print(list2[1:3])
print(list2[-4:-1])

# 3. Write a program to get the sum and multiply of all the items in a given list.
list3 = [1, 2, 3, 4, 5, 6, 7, 8]
total_sum = sum(list3)
print("Sum: ",total_sum)

result =1
for i in list3:
    result = i * result
print("Multiply list:", result)



# 4. Find the largest and smallest number from a given list.

list4 = [30, 2, 56, 7 , 19, 67, 5, 89]

max_list = max(list4)
print("Max: ", max_list)

min_list = min(list4)
print("Min:", min_list)


# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd =[]
for i in list5:
    if i%2==0:
        continue
    else:
        odd.append(i)
print("odd list",odd)



# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both included).

new_list = list(range(1,31))
print(new_list)

square_list =[]
for i in new_list:
    square_list.append(int(i*i))

print(square_list[:5])
print(square_list[-5:])



# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]

l1 = [1,3,5,7,9,10]
l2 = [2,4,6,8]

l1.pop()
l3 = l1+l2
print(l3)

# 8. Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}

a.update(b)
print(a)



# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

num = int(input("Enter any number: "))
dict ={}

for i in range(1, 1+num):
    dict[i] = i*i
print(dict)



# 10. Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)

num = input("Enter a sequence of numbers: ").split(',')

list_seq = list(num)
print(list_seq)

tup_seq = tuple(num)
print(tup_seq)