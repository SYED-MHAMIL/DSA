#!/bin/python3

import math
import os
import random
import re
import sys


# if __name__ == '__main__':
#     n = int(input().strip())

#     genes = input().rstrip().split()

#     health = list(map(int, input().rstrip().split()))

#     s = int(input().strip())
#     min_health =float('inf')
#     max_health =0

#     for s_itr in range(s):
#         first_multiple_input = input().rstrip().split()

#         first = int(first_multiple_input[0])

#         last = int(first_multiple_input[1])

#         d = first_multiple_input[2]
        
#         gen1=genes[first:last+1]
#         hel1= health[first:last+1]
#         total_health =0
        
#         for i,v in enumerate(gen1):
#             # aa in aaa
#             counter=0
#             start =0
#             while True:
#                 idx =d.find(v,start)
#                 if idx == -1 :
#                     break
#                 start= 1 +idx
#                 counter+=1
                
#             total_health+=counter *hel1[i]
            
#         max_health= max(max_health,total_health)
#         min_health = min(min_health,total_health)    
                    
#     print(min_health, max_health)        
            


# *************************************************************8 
                #  aobve is  corect but time limit exceed
# *************************************************************8 


#!/bin/python3

# import math
# import os
# import random
# import re
# import sys
# import re
# from collections import defaultdict


# if __name__ == '__main__':
#     n = int(input().strip())

#     genes = input().rstrip().split()

#     health = list(map(int, input().rstrip().split()))

#     s = int(input().strip())
#     min_health =float('inf')
#     max_health =0

#     for s_itr in range(s):
#         first_multiple_input = input().rstrip().split()

#         first = int(first_multiple_input[0])

#         last = int(first_multiple_input[1])

#         d = first_multiple_input[2]
        
#         # for start, end, dna in queries:
#     # Build map of gene -> list of health values at each position
#         gene_health_map = defaultdict(list)
#         for i in range(first, last + 1):
#             gene_health_map[genes[i]].append(health[i])

#         total_health = 0

#         for gene, health_list in gene_health_map.items():
#             # Use regex to find overlapping matches
#             matches = [m.start() for m in re.finditer(f'(?={gene})',d)]
#             count = len(matches)
#             total_health += count * sum(health_list)

#         # Track min/max health across all strands
#         min_health = min(min_health, total_health)
#         max_health = max(max_health, total_health)
                    
# print(min_health, max_health)        


# *****************************************************************
#  also above time exceed
# *****************************************************************


import ahocorasick
            
            
genes = ['a', 'b', 'c', 'aa', 'd', 'b']
health = [1, 2, 3, 4, 5, 6]
s = 3

queries = [
    (1, 5, "caaab"),
    (0, 4, "xyz"),
    (2, 4, "bcdybc")
]

min_health = float('inf')
max_health = 0

for start,end,dna in queries:
     A = ahocorasick.Automaton()
     for idx in range(start,end+1):
         gene =genes[idx]
         if A.exists(gene):
             A.get(gene).append((idx,health[idx]))
         else:
            A.add_word(gene, [(idx, health[idx])])  # store list of (index, health)
    
     A.make_automaton()

    # Total health for this DNA string
     total = 0

     for end_index, data in A.iter(dna):
        matches = data  # list of (index, health)
        for idx, h in matches:
            total += h

    # Track min/max
     min_health = min(min_health, total)
     max_health = max(max_health, total)

# Final output
print(min_health, max_health)
        
        
          
        
