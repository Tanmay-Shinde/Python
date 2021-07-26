"""Dice Game"""

import random
j=1
k=1

print("You need to get 6 to start the game going")
while True:
    inp = input("Enter y to roll the die: ")
    inp = inp.lower()
    if inp == 'y':
        num = random.randint(1, 6)
        print(num)
        if num == 6:
            break
        else:
            j+=1

print("You need to get an even number to keep the game going")
while True:
    inp1 = input("Enter y to roll the die: ")
    inp1 = inp1.lower()
    if inp1 == 'y':
        num2 = random.randint(1,6)
        print(num2)
        if num2%2!=0:
            print("Game Over")
            print("You rolled the die for ",j," times before starting the game")
            print("You rolled the die for ",k," times in the game")
            score = k*2 - j
            print("Your score is: ",score)
            break
        else:
            k+=1
