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
    
    
    # from itertools import permutations
# from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
          return False

        s1element,s2element = [0]*26,[0]*26
        for i in range(len(s1)):
            s1element[ord(s1[i])-ord("a")]+=1
            s2element[ord(s2[i]) -ord("a")]+=1
        
        match = 0  
        for i in range(26):
            match+=1 if (s1element[i]==s2element[i]) else 0

        
        l= 0 
        for r in range(len(s1),len(s2)):
            if match == 26:
               return True
            rIndex = ord(s2[r]) - ord("a")
            s2element[rIndex]+=1
            if s1element[rIndex] == s2element[rIndex]:
               match+=1
            elif s1element[rIndex]+1 == s2element[rIndex]:
                match-=1


            lIndex = ord(s2[l]) - ord("a")
            s2element[lIndex]-=1
            if s1element[lIndex] == s2element[lIndex]:
               match+=1
            elif s1element[lIndex]-1 == s2element[lIndex]:
                match-=1
            l+=1

        return match ==26   