# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 
            # print(r-l+1)

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


# def minSubArraayLen(target,nums):
# # Input: target = 7, nums = [2,3,1,2,4,3]

#     res = float('inf')
#     n= len(nums)
#     l=0
#     total = 0
#     for r in range(0,n):
#         total+=nums[r]
#         while total >= target:
#            res = min(res,r-l+1)
#            total-= nums[l]
#            l+=1
             
    
    
            
#     return   0 if isinstance(res,float) else res

# print(minSubArraayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))    



# def minSubArraayLen(target,nums):
# # Input: target = 7, nums = [2,3,1,2,4,3]

    # res = float('inf')
    # n= len(nums)
    # l=0
    # r=0
    # total = 0
    # while r< n:
    #     total+=nums[r]
    #     if total  < target:
    #        r+=1
    #     else:    
    #         while total >= target:
    #             res = min(res,r-l+1)
    #             total-= nums[l]
    #             l+=1
      
    #         r+=1
    
            
    # return   0 if isinstance(res,float) else res

# print(minSubArraayLen(target = 7, nums = [2,3,1,2,4,3]))    



