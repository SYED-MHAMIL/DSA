# def twoSum(arr,target):
    
#     for i in range(len(arr)):
#         for j in range(1+i,len(arr)):
#             sum = arr[i]+arr[j]
#             if sum == target:
#                 return [i,j]
#     return []

# print(twoSum([1,3,5,5],8))



# optimize way to solve it 

def twoSum(arr,target):    
    left=  0
    arr2=  arr
    obj = {}
    for i,v in enumerate(arr):
        obj[v]= i

    arr2.sort()
    right = len(arr) - 1
    while left<=right:
        sum = arr2[left] +arr2[right] 
        if sum == target:
            return [obj[arr2[left]],obj[arr2[right]]]
        elif sum > target:
            right-=1
        else:
            left+=1

print(twoSum([28,2,4,3,4],6))




# ******************************************************************
#               most   optimize  way  to  solove   it
# ******************************************************************

# arr = [1,2,4,3,4], target= 8

def twoSumoptimize(arr, target):
    indies  = {}
    for i,v in enumerate(arr):
        indies[v] =i 
    for j,val in enumerate(arr):
        diff = target - val
        if diff in indies and indies[diff] !=  j:
            return [j,indies[diff]]
    return []

# print(twoSumoptimize(arr =[28,2,4,3,4], target= 8))





# basically what i did in that example so lst's see okay
#  first thing is you have to do ovee fover it on array and the after that check the diff IS exites in obj so if not so add the value with index afte that iterate second index will check again the current diff si exsits in yoour obj if  exites retuurn current and find object value index                 


def twoSumoptimize2(arr, target):
    indies  = {}
    
    for j,val in enumerate(arr):
        diff = target - val
        if diff in indies:
            return [indies[diff],j]
        indies[val] = j
        
    return []

# print(twoSumoptimize2(arr =[4,5,3,4], target= 8))

