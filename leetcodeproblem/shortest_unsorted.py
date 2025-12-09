
def findUnsortedSubarray(nums):
         
        l =  0  
        n = len(nums) 
        # Input: nums = [2,6,4,8,10,9,15]
    #    [1,2,3,4]
        while l < n-1 and nums[l] <= nums[l+1]:
            l+=1
        
        if l == n-1:
           return 0 
        r =   n -1
        while r > 0 and nums[r] >= nums[r-1]:     
            r-=1
        return r-l + 1        
print(findUnsortedSubarray([1,2,3,4]))