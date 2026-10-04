# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date:
# Purpose: Create two lists and join them
# Usage: ./lab3c.py

# Follow the specific instructions given in the README.md file

mylist1 = []
mylist2 = []

# TODO 1: Create two lists, the first holding only odd numbers and the second holding only even numbers

#Odd list
for i in range (7): # 3 numbers
    if i%2 != 0:
       # print(i)
        mylist1.append(i)
print(mylist1) 

#Even list
for i in range (6): # 3 numbers 
    if i%2 == 0:
        # print(i)
        mylist2.append(i)
print(mylist2)

# TODO 2: Combine the two lists into one larger list using concatenation
mylist = mylist1 + mylist2

# TODO 3: Print out the new larger list
print(mylist)

