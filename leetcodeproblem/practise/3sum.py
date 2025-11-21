def threeSum(arrynum):
        res =  []
        nums= list(sorted(arrynum)) 
        for i in range(len(nums)-2):
            
            if i >  0 and  nums[i] == nums[i-1] :
               continue
            
            l = i+1
            r = len(nums) - 1
            target =-nums[i]

            while l < r: 
                sum = (nums[l]+nums[r])
                if target == sum:
                   res.append([nums[i],nums[l],nums[r]]) 
                   l+=1
                   r-=1   
                              
                elif  target > (l+r):
                    l+=1
                else:
                    r-=1
             
        return res
    
print(threeSum([-1,-1,-1,0,1,2]))