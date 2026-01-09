def minWindow( s, t) :
        n = len(s)
        left = 0
        res= []
        obj = {}
        for i in t:
           obj[i] = obj.get(i,0) + 1 

        for right in range(n):
            res.append(s[right])
            if s[right] in obj:
               if obj[s[right]] > 1:
                   obj[s[right]] -=1
               else:
                   del obj[s[right]]

            while len(obj)  == 0:
               res=min(res,list(s[left:right+1]))
               res.pop(left)
               
               left+=1 
               
            print("heloo lrft", left )
               
               
print(minWindow("ADOBECODEBANC" ,"ABC"))