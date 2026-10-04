# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: 
# Usage: ./lab3b.py

# Follow the specific instructions given in the README.md file

# TODO 1: Create the number list as specified in the README.md file
numberList = [1, 4, 9, 16, 9, 7, 4, 9, 11]
# TODO 2: Create a new empty list called reversed
reverse = []

# TODO 3: Use a for loop to add items from numbers list into reversed list in opposite order
# Loop thru the elemtns, (stat,stop,step) 
# Start at the last element, stop at -1 which is before the first index 0, because in range stops before the last number
# Step is -1 because it's backwards
for i in range(8,-1,-1):
    reverse.append(numberList[i]) # i is the index that we r appending from the numbers list in reverse
    # print(i)


# TODO 4: Confirm you have the right reversed list with print
print(reverse)