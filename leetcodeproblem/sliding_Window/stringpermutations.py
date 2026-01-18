from collections import Counter

def checkInclusion( s1: str, s2: str) -> bool:
        permutation =  {}
        for per in s1:
            permutation[per] =permutation.get(per,0) + 1 
        
        
        left = 0 
        right =  len(s1)
        n= len(s2)
        while right <= n:
             isContains = Counter(s2[left:right])
             print({"is conte" : isContains, "permuta" : permutation})   

             if isContains ==  permutation:
                return True
             left+=1
             right+=1

        return False
    
print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))