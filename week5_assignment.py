# create a credit card class with the following attributes: 
# card number, expiration date, and security code. Create a 
# method that will print out the card number, expiration date, 
# and security code. Create an instance of the class and call the method.
import secrets
from datetime import *
import os
import hashlib
import random
from dateutil.relativedelta import relativedelta

class Credit_card:
    def __init__(self, card_number, expiration_date, security_code):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code

    def create_card_number(self):

      card_number = '4567' + str(random.sample(range(33, 70), 6)) + datetime.now().strftime('%Y%m%d')

      return card_number

    def create_expiration_date(self):
      year = date.today()
      expiration_date = year + relativedelta(years=5)

      return expiration_date

    def create_security_code(self, card_number):
      return card_number[-3:]


results = Credit_card(44566666, 2023, 234)
results.create_card_number()
results.create_expiration_date()
results.create_security_code()

  


# create Animal class and Dog class. Make the Dog class inherit from the 
# Animal class. Add a bark method to the Dog class. Create an instance of the 
# Dog class and call the bark method.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age 

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)  
    
    def speak(self):
        print("Woa Woa")


molly = Dog("Tim", 5)
molly.speak()

# create a class called Queue. The class should have the following methods: 
# enqueue, dequeue, and size. The enqueue method should add an item to the queue. 
# The dequeue method should remove an item from the queue. The size method should 
# return the size of the queue.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q=Queue()	
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
q.dequeue()
print(q.size())

  
# create a class called Stack. The class should have the following methods: push, 
# pop, and size. The push method should add an item to the stack. The pop method 
# should remove an item from the stack. The size method should return the size of 
# the stack.

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)

    def pop(self):
        return self.elements.pop()

    def size(self):
       return len(self.elements)

stack = Stack()
stack.push(3)
stack.push(8)
stack.push("Elprofessor")
stack.push('test')
print(stack.pop())
print(stack.size())

# create a class called Person. The class should have the following attributes: 
# name, age, and address. The class should have the following methods: eat, sleep, 
# and work. The eat method should print out the name of the person and the word 
# "is eating". The sleep method should print out the name of the person and the word 
# "is sleeping". The work method should print out the name of the person and the word 
# "is working".

class Person():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def eat(self):
        print(self.name, "is eating")

    def sleep(self):
        print(self.name, "is sleeping")

    def work(self):
        print(self.name, "is working") 

person = Person("Elprofessor", 50, "Old Kira Road")
person.eat()
person.sleep()
person.work()


# create a class called Employee. The class should have the following attributes: 
# name, age, and salary. The class should have the following methods: eat, sleep,
#  and work. The eat method should print out the name of the person and the word
#  "is eating". The sleep method should print out the name of the person and the 
# word "is sleeping". The work method should print out the name of the person and 
# the word "is working". Create a subclass of Employee called Programmer. 
# The Programmer class should have the following attributes: name, age, salary,
#  and programming language. The Programmer class should have the following methods:
#  eat, sleep, work, and code. The code method should print out the name of the person
#  and the word "is coding in" and the programming language. Create an instance of the
#  Programmer class and call all the methods.

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def eat(self):
        print(self.name, "is eating")

    def sleep(self):
        print(self.name, "is sleeping")

    def work(self):
        print(self.name, "is working")

class Programmer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language  
    
    def code(self):
        print(self.name, "is coding in", self.programming_language)

person = Programmer("Elprofessor", 50, "$ 250,000", "Python")
person.eat()
person.sleep()
person.work()
person.code()



# create a class called Vehicle. The class should have the following attributes: 
# make, model, and year. The class should have the following methods: start, stop, 
# and drive. The start method should print out the make, model, and year of the 
# vehicle and the word "is starting". The stop method should print out the make, model,
#  and year of the vehicle and the word "is stopping". The drive method should print out
#  the make, model, and year of the vehicle and the word "is driving". Create a subclass 
# of Vehicle called Car. The Car class should have the following attributes: make, model, 
# year, and color. The Car class should have the following methods: start, stop, drive, 
# and park. The park method should print out the make, model, year, and color of the car 
# and the word "is parking". Create an instance of the Car class and call all the methods.

class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(self.make, self.model, self.year, "is starting")

    def stop(self):
        print(self.make, self.model, self.year, "is stoping")

    def drive(self):
        print(self.make, self.model, self.year, "is driving")


class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color 
    
    def park(self):
        print("Car of", self.make, self.model, self.year, "color", self.color, "is parking")

car = Car("Ford", "Bronco Sport", 2022, "Black")
car.start()
car.stop()
car.drive()
car.park()

# create a class called Animal. The class should have the following attributes: 
# name, color, and age. The class should have the following methods: eat, sleep, 
# and make_sound. The eat method should print out the name of the animal and the word
# "is eating". The sleep method should print out the name of the animal and the word 
# "is sleeping". The make_sound method should print out the name of the animal and the 
# word "is making a sound". Create a subclass of Animal called Dog. The Dog class should 
# have the following attributes: name, color, age, and breed. The Dog class should have 
# the following methods: eat, sleep, make_sound, and bark. The bark method should print
#  out the name of the dog and the word "is barking". Create an instance of the Dog 
# class and call all the methods.

class Animal():
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def eat(self):
        print(self.name, "is eating")

    def sleep(self):
        print(self.name, "is sleeping")

    def make_sound(self):
        print(self.name, "is making a sound")


class Dog(Animal):
    def __init__(self, name, color, age, breed):
        super().__init__(name, color, age)
        self.breed = breed 
    
    def bark(self):
        print(self.name, "is barking")

dog = Dog("Sherperd", "Black", "10 Years", "German")
dog.eat()
dog.sleep()
dog.make_sound()
dog.bark()

# create a class of your choice. It should have at least 3 attributes and 3 methods 
# where one of the methods is a static method. Implement polymorphism, encapsulation,
#  and inheritance.
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def eat(self):
        print(self.name, "is eating")

    def work(self):
        print(self.name, "is working")

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18

# Implementing inheristance
class Programmer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language  
    
    def code(self):
        print(self.name, "is coding in", self.programming_language)

# implementing Polymorphism
class Receiptionist(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary) 
    
    def duty(self):
        print(self.name, "is working at the front Desk")

person1 = Programmer("Elprofessor", 50, "$ 250,000", "Python")
person1.eat()
person1.work()
person1.code()
person1.isAdult(30)

print("/-------------------------------------------------------------/")

person = Receiptionist("Princess", 50, "$ 25,000")
person.eat()
person.work()
person.duty()
person.isAdult(22)