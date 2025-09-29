# Swap Two Numbers
# Last Updated : 23 Jul, 2025
# Given two numbers a and b, the task is to swap them.

# Examples:

# Input: a = 2, b = 3
# Output: a = 3, b = 2

# Input: a = 20, b = 0
# Output: a = 0, b = 20

# Input: a = 10, b = 10
# Output: a = 10, b = 10 


def swap_number(a,b):
    a,b=b,a
    print("a=", a,"b=",b)

swap_number(2,4)