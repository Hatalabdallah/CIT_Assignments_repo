# 1. Create a 2-D array and slice out the second number in the second column

array=[[23,45,43,23,45],[45,67,54,32,45],[89,90,87,65,44],[23,45,67,32,10]]

del(array[1][1])
 
print("New Array")

for _ in array:
    for x in _:
        print(x,end=" ")
    print()


# 2. Write a python program to sort array element in the ascending/descending order

size = int(input("Enter size of array: "))
arr = []
for i in range(size):
    element = int(input("enter element in array: "))
    arr.append(element)
    arr.sort()

print("Sorted array in ascending order is: ",arr)
print("Sorted array in Descending is: ", arr[::-1])

# 3. Write a python program to find the maximum and minimum value in a given 2-D array

import numpy as np

array = np.array([[23,45,43,23,45],[45,67,54,32,45],[89,90,87,65,44],[23,45,67,32,10]])
print(array)

max = np.max(array)
min = np.min(array)
print("The maximum value in the array is :",max)
print("The minimum value in the array is :",min)


'''4. Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
percentage less than 50 (Grade C)
percentage equal to 50 and less than 80 (Grade B)
percentage equal to 80 and more than 80 (Grade A)'''

sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))

avg = ((sub1+sub2+sub3+sub4+sub4)/500) * 100

if(avg >= 80):
    print("Grade: A")

elif(avg == 50 and  avg < 80):
    print("Grade: B")

elif(avg < 50):
    print("Grade: C")

else:
    print("You Failed!")


'''5. Write a python program to fetch only Email ID from text file which include following fields -:
# Name
# Mobile Number
# Roll Number
# Email ID '''
       
import re 
    
s =  open("test.txt",'r',encoding = 'utf-8')
    
contents = s.read()
    
lst = re.findall('[^,;\s]+@[^,;\s]+', contents)     
      
print(lst) 


'''6. Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point 
# and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended” '''

def check_speed(speed):
    if speed < 70:
        print("OK")

    elif speed > 70:
        points = (speed - 70) // 5
    
    if points > 12:
            print('License suspended')
    else:
         print('points = {}'.format(points))

check_speed(80)


''' 7.  Write a function called show_stars(rows). If rows is 5, it should print the following:
# *
# **
# ***
# ****
# ***** '''

num = int(input("Enter the number of rows: "))

for x in range(1, num+1):
    for y in range(1, x + 1):
        print("*" , end = "")
    print()


'''8. Write a program which will find all such numbers which are divisible 
# by 7 but are not a multiple of 5 between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line. '''

list=[]
for x in range(2000, 3201):
    if (x%7 == 0) and (x%5 != 0):
        list.append(str(x))
print (','.join(list))


''' 9. Write a program which accepts a sequence of 
# comma-separated numbers from console and generate a list and a 
# tuple which contains every number. Suppose the following input is 
# supplied to the program: 34,67,55,33,12,98 Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98') '''

values = input("Input some comma seprated numbers : ")

list = values.split(",")
tuple = tuple(list)

print('List : ',list)
print('Tuple : ',tuple)


''' 10. Write a program that calculates and prints the value according to the given formula: Q = Square root 
of [(2 * C * D)/H] Following are the fixed values of C 
and H: C is 50. H is 30. D is the variable whose values should be 
input to your program in a comma-separated sequence. 
Example Let us assume the following comma separated input sequence 
is given to the program: 100,150,180 The output of the program should be: 18,22,24 '''

import math
c=50
h=30
value = []
items=[x for x in input("Enter a lisit of numbers of your choice: ").split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

# 11. Write a function to compute 5/0 and use try/except to catch the exceptions.

def divide(x, y):
    try:
        result = x / y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

divide(5, 0)

# 12. Create a nesting list that prints out the color and the car brand.

Brand_color = [["BMW","FORD"], ["Black", "Green"]]

new_list = zip(*Brand_color)

print(list(new_list))

# 13. Bonus Question: Algorithm challenge: Create your own sorting algorihm.

def insert_sort(list):
    for i in range(1, len(list)):
        first_value = list[1]
        position = 1

        while position > 0 and list[position - 1] > first_value:
            list[position] = list[position - 1]
            position = position - 1

        list[position] = first_value
    return list

list = [2,0,8,56,3,13,76,9,77,23,11,76,87,45, 54,1,3,66]
print(insert_sort(list))