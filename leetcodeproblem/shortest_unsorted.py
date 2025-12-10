
def findUnsortedSubarray(nums):
         
        l =  0  
        n = len(nums) 
    #  Input: nums = [2,6,4,8,10,9,15]
    #  [1,3,2,2,2,4]
    #  [1,2,3,4,3,5,6,5,3,6,7,3,6,7,8]

        while l < n-1 and nums[l] <= nums[l+1]:
            l+=1
        
        if l == n-1:
           return 0 
        r =   n -1
        while r > 0 and nums[r] >= nums[r-1]:     
            r-=1
        
        min_value = min(nums[l:r+1])            
        max_value= max(nums[l:r+1])            
      
        while r < n-1 and nums[r+1] < max_value :
            r+=1
            
        while l > 0  and nums[l-1] < min_value :
            l-=1
                    
        return (r-l) + 1        
print(findUnsortedSubarray([1,3,2,2,2,4]))

