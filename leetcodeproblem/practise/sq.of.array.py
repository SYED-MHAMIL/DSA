# Input: nums = [-4,-1,0,3,10]

# Output: [0,1,9,16,100]    

def squareofArray(nums):
    positve,negative = [],[]
    
    for i in range(len(nums)):
        if  nums[i] > 0:
            positve.append(nums[i]) 
        else:
            negative.append(nums[i])
    
    if len(positve) == 0:
       return [i*i for i in negative].reverse()
    elif len(negative) == 0:
        return [i*i for i in positve]
    else:
        res = [] 
        l = 0 
        r =  0
        
        while  len(negative) > l  and len(positve) > r:
            if (negative[l]**2) < (positve[r]**2):
                res.append(negative[l]*negative[l])
                l+=1
            else:
                res.append(positve[r]*positve[r])
                r+=1
        
        while len(negative) > l:
            res.append(negative[l])
            l+=1
        
        while len(positve) > r:
            res.append(positve[r])
            r+=1
        
        return res 
                 
        
print(squareofArray([-4,-3,-2,-1,0,1,2,4]))
        
        
        
        
    
    

    
    
    
