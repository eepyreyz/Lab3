# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date:
# Purpose: 
# Usage: ./lab3g.py


# - Create an empty list
list = []
# - Create a while loop that ends when your list size reaches 6
userInput = 0
# - Add numbers to your list using input
# - Multiply the numbers by 10
# - Print out the list in reverse order

while len(list) != 6 :
    userInput = input("Enter a number: ")
    userInput = int(userInput)
    userInput *= 10
    list.append(userInput)
    #print(len(list))
    #print(list)

list.reverse()
print(list)
