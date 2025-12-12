def findUnsortedSubarray(nums):
    #  Input: nums = [2,6,4,8,10,9,15]
    #  [1,3,2,2,2,4]
    #  [1,2,3,4,3,5,6,5,3,6,7,3,6,7,8]
    l =0  
    n = len(nums)
    while l < n-1 and nums[l] <= nums[l+1] :
        l+=1
    
    r =n-1 
    while r > 0  and nums[r] >= nums[r-1] :
        r-=1     
    
    min_num = min(nums[l:r+1])
    max_num = max(nums[l:r+1])
    
    while l < n and nums[l-1] > min_num:
        l-=1
        
    while r > 0 and nums[r+1] < max_num:
        r+=1
    
    
    
    return r-l +1
    
            
print(findUnsortedSubarray([1,3,2,2,2,4]))

