# sample Game Guess

import os
import random

os.system("clear")

# colors
r = "\033[1;31m"
g = "\033[1;32m"
w = "\033[1;37m"

x = random.randint(1, 10)

run = True
while run:
    n = int(input("\033[1;37m ENTER THE NUMBER BETWEEN 1 AND 10: "))

    if n > 10 or n < 1:
        print("\n Please enter the number between 1 and 10. \n")
        run = False

    elif n == x:
        print(g,"\n YOU WON", f"The number is {x}. \n",w)
        run = False

    elif n > x:
        print(r,"\n The number is small \n",w)
        
    elif n < x:
        print(r,"\n The number is big \n",w)