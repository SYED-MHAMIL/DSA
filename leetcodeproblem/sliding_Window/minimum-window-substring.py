def minWindow( s, t) :
        n = len(s)
        left = 0
        res= float('inf')
        requirement = {}
        need = {}
        for i in t:
           requirement[i] = requirement.get(i,0) + 1 

        for right in range(n):
            if s[right] in requirement:
               need[s[right]] =  need.get(s[right],0)+1
                 
            while isRequirementFull:=  all( need.get(c,0) >= requirement[c] for c in  requirement):
               res=min(res, right-left+1)
               if s[left] in requirement:
                   if need.get(s[left],0) > 1:
                      need[s[left]]-=1
                   else:
                        del need[s[left]]  
               left+=1 
               
        return "" if isinstance(res,float) else res   
print(minWindow( "ADOBECODEBANC", t = "ABC"))  