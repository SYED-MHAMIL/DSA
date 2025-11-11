def removeDuplicates(nums) :
        # officernextroom = check_dup = 1
        # n = len(nums)
        # count =1

        # if nums[0] == nums[check_dup]:
        #    check_dup += 1 

        # while check_dup < n :
            
        #     if  nums[officernextroom] == nums[check_dup]:
        #         check_dup += 1
        #     else:
        #             nums[officernextroom] = nums[check_dup]
        #             officernextroom+=1
        #             check_dup+=1
        #             count+=1
        # return count,nums
        
        
        
        
        l=r=0
        n = len(nums)
        
        while r< n:
            nums[l] = nums[r]
            [1,2,3,3]
            while r < n  and  nums[l] == nums[r] :
                  r+=1
            l+=1  
                 
        return  l,nums,r
         
    # [1,2,3,3,3,4]
print(removeDuplicates([1,1,2,3,3,4]))