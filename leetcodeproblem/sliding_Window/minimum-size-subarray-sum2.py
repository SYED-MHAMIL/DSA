class Solution:
    def minSubArrayLen(self, target, nums) :
     n = len(nums)
     left =  0
     res = float('inf') 
     
     sum = 0 
     for right in range(n):
         sum+=nums[right]

         if sum <target:
            right+=1
         else:
            while sum >= target:
                res = min(res,right-left+1)
                sum-=nums[left]
                left+=1
            right+=1
     return  0 if isinstance(res,float) else res
                    
                    
    