# You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.
# Note : If no such substring exists, return -1. 


# def longestKSubstr(s, k):
#     # code here
# #   first step will be take out the length
# #  second we will make the varibale  that take the longest substring
# #  we will put it there loop  for 
#     n = len(s)
#     res = -1
    
#     for l in range(n):
#         obj={}
#         for r in range(l,n):
            
#             obj[s[r]] = obj.get(r,0)+1
#             if len(obj) == k:
#                 res = max(res,r-l+1)
#             elif len(obj) > k:
#                 break
                 
#     return  -1 if (res < k) else  res
# print(longestKSubstr("aaba{cbe]bebe",3))



def longestKSubstr(s, k):
        # code here
    #   first step will be take out the length
    #  second we will make the varibale  that take the longest substring
    #  we will put it there loop  for 
        # ebngqsoagt{ufqifwf}
      
      
          
      # Example 1:

      # Input: fruits = [1,2,1]
      # Output: 3
      # Explanation: We can pick from all 3 trees.
      # Example 2:

      # Input: fruits = [0,1,2,2]
      # Output: 3
      # Explanation: We can pick from trees [1,2,2].
      # If we had started at the first tree, we would only pick from trees [0,1].
      # Example 3:

      # Input: fruits = [1,2,3,2,2]
      # Output: 4
      # Explanation: We can pick from trees [2,3,2,2].
      # If we had started at the first tree, we would only pick from trees [1,2].        

        n = len(s)
        res = 0
        obj={}
        l= 0 
        r=0 
        
        while r < n :
          
            obj[s[r]] = obj.get(s[r],0) +1
            # print("obj",obj) 
            if len(obj) <= k:
                res = max(res,r-l+1)
                r+=1
            elif len(obj) > k:
              while not (len(obj) <= k):

                print("index",l)  
                if obj[s[l]] == 1:            
                   del obj[s[l]]
                else:
                    obj[s[l]] -= 1
                print(obj)
                l+=1
              r+=1
                        
                
        return    res
    
print(longestKSubstr(s = [0], k = 2))
