# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/10/04
# Purpose: 
# Usage: ./lab3a.py

# TODO 1: Import the random module
import random

# TODO 2: Create an empty list called numbers
numbers = []
# TODO 3: Create a for loop that generates 20 random numbers between 0 and 99, and adds them to our numbers list 
for i in range (20):
    i = random.randint(0, 99)
    numbers.append(i)
    # print(numbers)

# TODO 4: Print the numbers list, then sort it in lowest to highest order, and print it once more.
print(numbers)
numbers.sort()
print(numbers)

