# for k sorted




numbers = [0,0,1,1,1,4,4,4,4]

def removeDup(nums,k=3) ->None:
    l,r = 0,0 
    
    while r < len(nums):
        count =1
        while r+1 < len(nums) and  nums[r] == nums[r+1]:
            count+=1
            r+=1
        for i in range(min(k,count)):
            nums[l] = nums[r]
            l+=1
            
        r+=1
        
    return l 

        
        
print(removeDup(numbers))