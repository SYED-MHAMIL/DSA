# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 

# Constraints:


def minSubArraayLen(target,nums):
# Input: target = 7, nums = [2,3,1,2,4,3]
    
    res = float('inf')
    n= len(nums)
    l=0
    r=0
    value = 0
    
    while r < n and  l<=r :
        value+=nums[r]
        if(value < target):
             r+=1
        else:
            # print(r-l+1)
           while value >= target: 
                res = min(res,r-l+1)
                value-=nums[l]
                l+=1
           r+=1
            
    return   0 if isinstance(res,float) else res

print(minSubArraayLen(target = 7, nums = [2,3,1,2,4,3]))