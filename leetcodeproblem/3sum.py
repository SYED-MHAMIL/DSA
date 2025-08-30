def threeSum(nums):
    arr= []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                sumNum = nums[i]+nums[j]+nums[k]
                if sumNum == 0 :
                    arr.append([nums[i],nums[j],nums[k]])
    return arr

print(threeSum([-3,3,4,-3,1,2]))
