from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permutation =  []
        for per in permutations(s1):
            permutation.append("".join(per))
        
        left = 0 
        right =  len(s1)
        n= len(s2)
        while right <= n:
             isContains = s2[left:right]
             if isContains in permutation:
                return True
             left+=1
             right+=1

        return False