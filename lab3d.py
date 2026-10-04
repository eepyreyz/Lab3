# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/10/04
# Purpose: Practice adding and removing elements in list.
# Usage: ./lab3d.py

# - Create a variable `mylist` that conatins  first 6 natural numbers.
mylist = [1,2,3,4,5,6]

# - Use the `append()` method and add a new element, number 7 in the variable `mylis`t. 
mylist.append(7)

# - Use the `inser()` method and insert the element 0 at index 0.
mylist.insert(0,0)

# - Use the `pop()' method to remove the element from index 2.
mylist.pop(2)

# - Print the variable `mylist`.
print(mylist)

# - Add another statement in the script to find the index of the element 6 and print `The element 6 is present at the index ---`
for i in mylist:
    if i == 6:
        # print(i) the element
        # print(mylist[i]) Its index
        print(f"The element 6 is present at the index {mylist[i]}")

