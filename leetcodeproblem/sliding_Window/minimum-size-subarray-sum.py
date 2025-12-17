def minSubArrayLen(target,nums):
    res = 100000000000000000
    n= len(nums)
    l=0
    r=0
    while r< n :
        value= sum(nums[l:r+1])
        if value < target:
            r+=1
        else:
            res=  min(res, len(nums[l:r+1]))
            while value < target and l < r:
                l+=1    

    return res      
     

print(minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))