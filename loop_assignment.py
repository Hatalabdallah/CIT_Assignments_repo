# #1. Print first 10 numbers using while loop
counter = 0
while counter <= 10:
    print(counter)
    counter = counter + 1
    
# #2. Calculate the sum of all numbers from 1 to a given number.
counter = 0
total = 0
while counter<10:
    total += counter
    counter += 1
print(total)

# #3. Write a program to print multiplication table of a given number. eg if number is 2, then output should be 2, 4, 6, 8 ..
n = 2
for i in range(1, 11, 1):
    product = n * i
    print(product)

# # 4. Write a program to display only those numbers from a list that satisfy
# # the following conditions
# # The number must be divisible by five
# # If the number is greater than 150, then skip it and move to the next
# # number
# # If the number is greater than 500, then stop the loop
# # given 'numbers = [12, 75, 150, 180, 145, 525, 50]:
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)

# #5. Write a program to count the total number of digits in a number using
# # a while loop. given number *4673453°
num = 4673453
var = 0
while num != 0:
    num = num // 10
    var = var + 1
print("Total number of digits are:", var)

#6. Display numbers from -10 to -1 using while loop
counter = -1
while counter >= -10:
    print(counter)
    counter = counter - 1
