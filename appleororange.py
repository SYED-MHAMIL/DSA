#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s --> sam house location starting point
#  2. INTEGER t --> sam house location ending point
#  3. INTEGER a --->  location of apple tree
#  4. INTEGER b  --->  location of oranges tree
#  5. INTEGER_ARRAY apples 
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    sam_Location = list(range(s,t+1))
    # location of apple tree
    count_apple=0
    count_oranges=0
    for i in range(len(apples)):
        # global sam_Location,count_apple
        sumer=a+apples[i]
        if s<= sumer <=t:
           count_apple+=1
            
    for i in range(len(oranges)):
        sumer=b+oranges[i]
        if s<= sumer <=t:
           count_oranges+=1
           
    print(count_apple)
    print(count_oranges)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
