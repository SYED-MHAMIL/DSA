# from collections import Counter
# # O(m*n) alorithms
# def checkInclusion( s1: str, s2: str) -> bool:
#         permutation =  {}
#         for per in s1:
#             permutation[per] =permutation.get(per,0) + 1 
        
        
#         left = 0 
#         right =  len(s1)
#         n= len(s2)
#         while right <= n:
#              isContains = Counter(s2[left:right])
#              print({"is conte" : isContains, "permuta" : permutation})   

#              if isContains ==  permutation:
#                 return True
#              left+=1
#              right+=1

#         return False
    
# print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))



# from itertools import permutations
# from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation =  {}
        for per in s1:
            permutation[per] =permutation.get(per,0) + 1 
        
        left = 0 
        right =  len(s1) -1
        n= len(s2)
        isContains ={}
        for i in s2[left:right+1]:
            isContains[i]=isContains.get(i,0) + 1
        
        while right < n:  
             if isContains ==  permutation:
                return True
             if isContains[s2[left]] > 1:
                isContains[s2[left]]-=1
             else:
                 del isContains[s2[left]]
             left+=1
             right+=1
             if right <n:
                isContains[s2[right]]=isContains.get(s2[right],0) + 1

        return False
    
    # almost 0(n)