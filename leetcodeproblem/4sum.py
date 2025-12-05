class Solution:
    def fourSum(self, nums, target: int):  
        nums.sort()
        res = [] 
        n = len(nums)
        for i in range(n-3):
            if i and nums[i] == nums[i-1] :
               continue 
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1] :
                    continue 

                l = j+1
                r = n-1
                while l < r:
                    sum = nums[i] +nums[j] +nums[l] +nums[r] 
                    if target == sum :
                       res.append([nums[i],nums[j],nums[l] ,nums[r]])
                       l+=1
                       r-=1
                       while l <r and  nums[l] == nums[l-1]:
                            l+=1

                       while l  <  r and nums[r]  == nums[r+1]:
                            r-=1
                    elif target>sum :
                         l+=1
                    else:
                        r-=1 
        return res