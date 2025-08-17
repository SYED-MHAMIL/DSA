# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

    # 1 <= nums.length <= 10^4.
    # -1000 <= nums[i] <= 1000
    # 1 <= k <= number of distinct elements in nums.








# ***************************************************************
#                   Brute force
# ***************************************************************






def k_frequency(arr,k):
# Input: nums = [1,2,2,3,3,3], k = 2
     
    #  arr =[]
    obj = {}
    for i in range(len(arr)):
        obj[arr[i]]= obj.get(arr[i],0) +1 

    sorted_arr = [key for key,val in sorted(obj.items(),reverse=True,key=lambda x:x[1])][:k]
    return sorted_arr

k_frequency([1,2,2,3,3,3],k = 2)     

