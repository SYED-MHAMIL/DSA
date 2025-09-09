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

    # arr= set()
    arr = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sumNum = -(nums[i]+nums[j])
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    # sort_val = tuple(sorted([nums[i],nums[j],nums[k]]))
                    arr.append([nums[i],nums[j],nums[k]])
    return list(arr)

# print(threeSum1([-1,0,1,2,-1,-4]))



# **************************************************************************************
#                          Two poinmter + sort
# **************************************************************************************




def threeSumbySorting(nums):
    sorted_val =  sorted(nums)
    res = []
    for i in range(len(sorted_val)):
        target = -sorted_val[i]
        sublist= sorted_val[i+1:] 
        left,right =0, len(sublist)  -1  
        while left < right :
            sumof = sublist[left] + sublist[right]
            if target == sumof:
                print("get")
                res.append([sorted_val[i],sublist[left],sublist[right]])
                break
            elif sumof > target:
                right-=1
            else:
                left+=1
                
    return res

print(threeSumbySorting([-1,0,1,2,-1,-4]))
