#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())
    min_health =float('inf')
    max_health =0

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        
        gen1=genes[first:last+1]
        hel1= health[first:last+1]
        total_health =0
        
        for i,v in enumerate(gen1):
            # aa in aaa
            counter=0
            start =0
            while True:
                idx =d.find(v,start)
                if idx == -1 :
                    break
                start= 1 +idx
                counter+=1
                
            total_health+=counter *hel1[i]
            
        max_health= max(max_health,total_health)
        min_health = min(min_health,total_health)    
                    
    print(min_health, max_health)        
            


# *************************************************************8 
                #  aobve is  corect but time limit exceed
# *************************************************************8 
            
            
            
        
        
        
        
          
        
