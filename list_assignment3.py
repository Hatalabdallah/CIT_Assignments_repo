# 1. Write a Python program to sum all the items in a list.
#     - The list should be generated using list comprehension
#     - The size of the list should be from a user input

# user = int(input("Enter list range: "))
# list = [for x in in range(user) if x / 1 == x]
# print(list)
# print(sum(list))

sum_items = 0

user = int(input("Enter number Range of choice: "))
n = list(range(user))

for item in range(0, len(n)):
    sum_items = sum_items + n[item]

print("Sum of all elements in given list: ", sum_items)

# 2. Write a Python program to count the number of strings where the string length is 2 or 
# more and the first and last character are same from a given list of strings. Sample List : 

string_list = ['abc', 'xyz', 'aba', '1221']
count = 0
for x in string_list:
    if len(x) > 1 and x[0] == x[-1]:
        print(x)
        count += 1

print("The Number of strings with length 2 and above with same 1st and 2nd character is: ", count)

# 3. Write a Python program to remove duplicates from a list, given list

fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]

result=[]  
 
for i in fruits:
    if i not in result:
        result.append(i) 
  
print("The result after removing duplicates is ",result)

# 4. Write a Python program to print a specified list after removing the 0th, 4th 
# and 5th elements. Sample List : `

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list.pop()

del list[0:5:4]

print(list)


# # 5. Write a Python program to generate and print a list except for the first 5 elements, 
# # where the values are square of numbers between 1 and 30 (both included)
# # Make a list of 1 10 30 where from 6 to 30 are square numbers

list = []

for i in range(1,6):
    list += [i]

for i in range(6,31):
    list += [i**2]

print(list) 