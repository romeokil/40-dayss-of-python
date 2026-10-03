# Day -12 Guessing Game
import random

num = int(input("Enter Your Guessing No: "))
random_Num = random.randint(1,100)
no_Of_Attempts=0
while num!=random_Num:
    if num>random_Num:
        print('Please guess lower')
    else:
        print('Please guess higher')
    
    no_Of_Attempts+=1
    num = int(input("Enter Your Guessing No: "))

print("Well Done", "You guess right", random_Num)
print("You have taken ",no_Of_Attempts," attempts")