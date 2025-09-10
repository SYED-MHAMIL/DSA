# **************************************************************************************
#                          Brute force  
# **************************************************************************************



def threeSum(nums):

    # arr= set()
    arr = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sumNum = -(nums[i]+nums[j])
            for k in range(j+1, len(nums)):
               if sumNum == nums[k]:
                    # sort_val = tuple(sorted([nums[i],nums[j],nums[k]]))
                    arr.append([nums[i],nums[j],nums[k]])
    return list(arr)

# print(threeSum([-1,0,1,2,-1,-4]))

def threeSum1(nums):

    arr= set()
    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sumNum = -(nums[i]+nums[j])
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    sort_val = tuple(sorted([nums[i],nums[j],nums[k]]))
                    arr.add(sort_val)
    return [list(i)   for i in  arr ]

# print(threeSum1([-1,0,1,2,-1,-4]))







# *********************************************************************#                          hash map + sort *******************************************************************
from collections import defaultdict
def threeSumUsingHash(nums):
    count = defaultdict(int)
    nums.sort()     


    
    return nums
print(threeSumUsingHash([-1,0,1,-1,-4]))    




def threeSum( nums):
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        res = []
        for i in range(len(nums)):
            count[nums[i]]-=1
            if i and nums[i] == nums[i -1]:
                continue
            for j in range(i+1 , len(nums)):
                count[nums[j]]-=1
                if j-1 > i and nums[j] == nums[j -1]:
                    print("cotinue when jth and less than jth are equal")
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0 :
                   res.append([nums[i],nums[j],target]) 
            print(count)   
                            
            for j in range(i+1,len(nums)):
                    count[nums[j]]+=1
    
    
        return res    

print(threeSum([-4, -1,-1, 0, 1, 2]))
                #i,           j

















# **************************************************************************************
#                          Two poinmter + sort
# **************************************************************************************




# def threeSumbySorting(nums):
#     sorted_val =  sorted(nums)
#     print("sorted value ", sorted_val)
#     res = set()
#     for i in range(len(sorted_val)):
#         target = -sorted_val[i]
#         sublist= sorted_val[i+1:] 
#         left,right =0, len(sublist)-1  
#         while left < right :
#             sumof = sublist[left] + sublist[right]
#             if target == sumof:
#                 print("get")
#                 sorted_res =sorted([ sorted_val[i],sublist[left],sublist[right]]
#                 )
#                 print(sorted_res)
#                 res.add(tuple(sorted_res))
                
#                 left+=1
#                 right-=1
#             elif sumof > target:
#                 right-=1
#             else:
#                 left+=1
                
#     return [list(i) for i in res]

# print(threeSumbySorting([-1,0,1,1,-1,-4]))
