# brute force 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res =  0
        n = len(s)

        for left in range(n):
            # Input: s = "ABAB", k = 2
            maxCount =  0 
            hashMap = {}
            for right in range(left,n):
                hashMap[s[right]] =hashMap.get(s[right],0)  + 1
                maxCount = max(maxCount,hashMap[s[right]])
                hastobeReplaced = (right - left + 1)-maxCount
                abletoReplaced = k - hastobeReplaced   

                if abletoReplaced>=0:
                   res = max(res, right - left + 1)
                else:
                    break
        
        return res
    
    
