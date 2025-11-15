# nums=[0, 1,0, 0, 0, 0, 3, 0, 12,0]
# newA= []    
# count=0




# for n in range(len(nums)):
#     if nums[n]==0:

#        newA.append(nums[n])
#     else:
#         newA.insert(count,nums[n])
#         count+=1

# print(newA)




# practise  

# for i in range(len(nums)):
#     if nums[i] == 0:
#         newA.append(nums[i])
#     else:
#         newA.insert(count,nums[i])
#         count+=1

# print(newA)



# zeromove with two pointer

nums = [0,1,0,3,12]
# def move_zero(arr):
#     # if len(arr) <= 1:
#     #     return arr  

#     l,r = 0,1
    
#     while r < len(arr):
#         if nums[r] != 0:
#            zero = arr[l]
#            arr[l] = arr[r]
#            arr[r]  = zero 
#            r+=1
#            l+=1
        
#         while  r< len( arr) and  nums[r] == 0 :
#             r+=1 
        
      
#     return arr    
# print(move_zero(nums))           







# other way but same tow pointer 

def move_zero(arr):
    if len(arr) <= 1:
        return arr  

    l = 0
    for r in range(1,len(arr)):
        if arr[r] != 0:
           arr[l] = arr[r]
           l+=1
    
    while l < len(nums):
        nums[l] = 0 
        l+=1       
    
    
      
    return arr    
print(move_zero(nums))           




