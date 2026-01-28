class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:      
        if len(p) > len(s):
            return []
        sele = [0] * 26
        pele = [0] * 26

        for i in range(len(p)):
            sele[ord(s[i]) - ord("a")] +=1
            pele[ord(p[i]) - ord("a")] +=1
        
        match = 0
        result = [] 
        for i in range(26):
            match+= 1 if  pele[i] == sele[i] else 0

        l= 0
        for r in range(len(p),len(s)):
            if match == 26:
               result.append(l)
        #    move left 
            index = ord(s[l]) - ord("a")
            sele[index] -=1

            if sele[index] == pele[index]:
                match+=1
            elif sele[index] == pele[index]-1:
                match-=1
            l+=1

    #       move right 
            index = ord(s[r]) - ord("a")
            sele[index] +=1

            if sele[index] == pele[index]:
                match+=1
            elif sele[index] == pele[index]+1:
                match-=1 
          
            
        if  match == 26:
            result.append(l)
        return result             