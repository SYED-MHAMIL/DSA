nums=[0, 1,0, 0, 0, 0, 3, 0, 12,0]
newA= []    
count=0
# for n in range(len(nums)):
#     if nums[n]==0:

#        newA.append(nums[n])
#     else:
#         newA.insert(count,nums[n])
#         count+=1

# print(newA)




# practise  

for i in range(len(nums)):
    if nums[i] == 0:
        newA.append(nums[i])
    else:
        newA.insert(count,nums[i])
        count+=1

print(newA)