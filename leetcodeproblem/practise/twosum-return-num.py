# Input: nums = [11,15,2,7], target = 9
# Output: [0,1]


nums = [11,15,2,7]
def sumup(nums,target = 17):
    sorted_list = sorted(nums)
    i = 0 
    j = len(sorted_list) - 1
    
    while i < j:
        sum = sorted_list[i] + sorted_list[j]  
        if sum == target:
           return  [sorted_list[i], sorted_list[j]]
        elif  sum > target:
            j-=1
        else:
            i+=1
              
        
        
    
print(sumup(nums))