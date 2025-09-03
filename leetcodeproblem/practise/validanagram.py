class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        bucket1 = [0] *26
        bucket2 = [0] *26
        for ch in s:
                bucket1[ord(ch)-ord('a')]+=1
         
        for ch in t:
                bucket2[ord(ch)-ord('a')]+=1
        
        return bucket1 == bucket2



# Brut force method


# def validAnagram(s,t):
#     if len(s) != len(t):
#          return False
    
#     sorted_S = sorted(s)
#     sorted_t = sorted(t)
#     return sorted_S == sorted_t

# print(validAnagram('hello','ogleh'))




# *************************************************************
# from  haash map 
# *************************************************************

def valisAnagram(s,t):
    freq = [0] * 26
    if len(s) != len(t):
         return False
    for index in range(len(s)):
        freq[ord(s[index]) - ord('a')]+=1
        freq[ord(t[index]) - ord('a')]-=1
    for l in freq:
        if l != 0 :
           return False
    return True


print(valisAnagram('manga','namgr'))
         

                                                     


