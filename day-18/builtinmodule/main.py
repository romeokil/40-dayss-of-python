# Day - 18 Built in Module

# file containing a function which may you can use in your application 

# example modules -> Math, Random , os , time

# to list all the modules
# help('modules')

# math module
import math

print(math.factorial(4))

print(math.ceil(2.4))

print(math.floor(2.8))

print(math.sqrt(2))

# random module
import random 

random_Num = random.randint(1,100)

a =[1,2,3,4,5]
random.shuffle(a)
print(a)
print(random_Num)

# time module
import time

print(time.time())
print(time.ctime())
print("Hello")
time.sleep(3)
print("World")

# os module
import os 

print(os.getcwd())
print(os.listdir())