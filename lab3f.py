# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: 
# Usage: ./lab3f.py

# Follow the specific instructions given in the README.md file

# TODO 1: Copy the matrix code from the README.md file
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# TODO 2: Print out the element with the value 5 from this matrix
print(matrix[1][1])

# TODO 3: Print out the element with the value 2 from this matrix
print(matrix[0][1])

# TODO 4: Print out the element with the value 9 from this matrix
print(matrix[2][2])

# TODO 5: Use a nested for loop to print out each value from the matrix on a separate line

rows = len(matrix) # Elements number in the list is the rows
# print(rows)

columns = len(matrix[0]) # Elements num in row 0 is the columns number 
# print(columns)
print("-" * 15)
for i in range (rows): # i is row index
    for j in range (columns): # j is column index
        print(matrix[i][j])

