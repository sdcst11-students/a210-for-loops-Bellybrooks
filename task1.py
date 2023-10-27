#!python3 

"""
##### Task 1
Ask the user to enter an integer.
Print the multiplication tables up to 12 for that number
using a for loop instead of a while loop.
hint:
using a print statement with the optional parameter:
,end="" 
will help you print things on the same line.

Example:
print("Hello", end="")
print("This is on the same line")
(2 points)

inputs:
int number

outputs:
multiples of that number

example:
Enter number:4
4 8 12 16 20 24 28 32 36 40 44 48
"""

for i in range(10):
  double = 4 * i
  print(f"The number right now is {i} and its doubled value is {i}")
else:
  print("We are finished!")
