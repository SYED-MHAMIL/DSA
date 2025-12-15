# Input: arr[] = [100, 200, 300, 400], k = 2
# Output: 700
# Explanation: arr2 + arr3 = 700, which is maximum.

# def max_sum_subarray(nums,k):
#     low = 0 
#     high =k-1 
#     n = len(nums)
#     max_value  = sum(nums[low:high+1])
    
#     while high < n:
#         low+=1
#         high+=1        
#         max_value = max(max_value,sum(nums[low:high+1]))    
#     return max_value

# print(max_sum_subarray([100,200,300,400],2))



def max_sum_subarray(nums,k):
    low = 0 
    high =k-1 
    n = len(nums)
    sum_up  = sum(nums[low:high+1])
    res = 0 
    while high < n:
        res = max(res,sum_up)    
        low+=1
        high+=1        
        if high == n :
           break 
        sum_up-=nums[low-1]
        sum_up+=nums[high]
    return res


print(max_sum_subarray([100,500,300,400],2))