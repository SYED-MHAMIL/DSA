
## Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.




# =====================================================================================
    #                        Brute force
# =====================================================================================



# def numSubarrayProductLessThanK(nums,k):
#     n=len(nums)
#     res = 1 
#     for i in range(n):
#         pow =1
#         for j in range(i,n):
#             pow*= nums[j]
#             if pow >= k :
#                break
#             res+=1
            



# =====================================================================================
#                        TWO POINTER METHOD
# =====================================================================================


def numSubarrayProductLessThanK(nums,k):
    n=len(nums)
    res = 0
    l=0  
    prod =1
    # Input: nums = [10,5,2,6], k = 100
    for r in range(n):
        prod*= nums[r]
        # 10 ,5 
        while prod >= k: 
            # L=0 =10 ,5
            prod//= nums[l] # 1
            l+=1
        res += (r -l )+1   
    return res  


print(numSubarrayProductLessThanK([10,5,2,6],100))    