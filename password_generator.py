# Password Generator Python Project Create a program that generates a 
# random password for the user. Ask the user how long they want their 
# password to be, and how many letters and numbers they want in their password. 
# ave a mix of upper and lowercase letters, as well as numbers and symbols. T
# he password should be a minimum of 6 characters long.

import random
import string
import time

print("\n\nPASSWORD GENERATOR!\n\n")
time.sleep(2)

passlen = int(input("How long should your password be? : \n"))
time.sleep(1)

letterlen = int(input("How many letter do you want in your password? : \n"))
time.sleep(1)

numlen = int(input("How many numbers do you want in your password? : \n"))
time.sleep(1)

symlen = passlen - (letterlen + numlen)

finallen = letterlen + symlen + numlen
x = ""

for i in range(letterlen):
    x = x + random.choice(string.ascii_lowercase + string.ascii_uppercase)


for i in range(symlen):
    x = x + random.choice(string.punctuation)


for i in range(numlen):
    x = x + random.choice(string.digits)

if finallen != passlen: print("Invalid length")
x = ''.join(random.sample(x, finallen))

print("Your password is {}". format(x))
