def minWindow( s, t) :
        n = len(s)
        left = 0
        res= s.split()
        obj = {}
        for i in t:
           obj[i] = obj.get(i,0) + 1 

        for right in range(n):
            
            if s[right] in obj:
               if obj[s[right]] > 1:
                   obj[s[right]] -=1
               else:
                   del obj[s[right]]
            
            print("element" ,s[right])
            
            
            while len(obj)  == 0:
               res=min(res,list(s[left:right+1]))
               print("Res", res)
               if s[left] in t:
                   obj[s[left]] = obj.get(s[left],0) + 1  
               print("obj fareq" ,obj )
                   
               print("left pointer" ,left )
               left+=1 
               
        return res     
print(minWindow("ADOBECODEBANC" ,"ABC"))