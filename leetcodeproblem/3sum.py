# **************************************************************************************
#                          Brute force  
# **************************************************************************************



def threeSum(numsArray):

    # arr= set()
    arr = []
    nums = list(sorted(numsArray))
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

# print(threeSum([-4, -1,-1, 0, 1, 2]))
                #i,           j

















# **************************************************************************************
#                          Two poinmter + sort
# **************************************************************************************




def threeSumbySortingTwopointer(numsAttay):
    res= []
    nums = sorted(numsAttay)
    for i in range(len(nums)-2):
        #  skip duplicate --->  lets suppose [-4,-1,-1,-1,-1, 0, 1,2] 
                                                    
        if i and  nums[i-1]  == nums[i]:
            continue

        left,right = i+1, len(nums) -1
        while left <right:
            target = -(nums[i])
            sum = nums[left] +nums[right]
            if target == sum:
               res.append([nums[i],nums[left] ,nums[right]])
               left+=1
               right-=1
        #  skip duplicate left --->  lets suppose [-4,-1,-1,-1,-1, 0, 1,2,2,2,2,2] 
               while left <right and nums[left] == nums[left-1]:
                      left+=1
        #  skip duplicate right --->  lets suppose [-4,-1,-1,-1,-1, 0, 1,2,2,2,2,2] 
               while left <right and nums[right] == nums[right+1] :
                   right-=1
            elif target > sum:
                 left+=1
            else:
                right-=1
    return res


print(threeSumbySortingTwopointer([-1,-1,-4,0,1,2]))