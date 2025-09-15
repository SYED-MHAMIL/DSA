# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.
# Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?



def findMin( nums):
        # Input: nums = [3,4,5,6,1,2]
                            #m 
    res = nums[0]
    l =  0
    r = len(nums) -1  
    
    while l <= r:
        if nums[l] < nums[r]:
           res = min(res,nums[l])
           print("stop")
           break
        # print("bahir") 
        m = (l+r) // 2
        res= min(res,nums[m])    
        if nums[m] >= nums[l]:
            l=m+1
        else:
            r= m-1
             
    return res 

 
print(findMin([4,5,0,1,2,3]))


# yoiu can also check from right side 

def findMin( nums):
        # Input: nums = [3,4,5,6,1,2]
    print("check from the right pointer ")                        #m 
    res = nums[0]
    l =  0
    r = len(nums) -1  
    
    while l <= r:
        if nums[l] < nums[r]:
           res = min(res,nums[l])

           break
        # print("bahir") 
        m = (l+r) // 2
        res= min(res,nums[m])    
        if nums[m] >= nums[r]:
            l=m+1
        else:
            r= m-1
             
    return res 

 
print(findMin([4,5,0,1,2,3]))



def findMinOther(nums):
    print("printed")
    l = 0 
    r = len(nums)  -1
    res = nums[0] 
    while l <= r:
      if nums[l] < nums[r]:
        res = min(res,nums[l])
        break
    #   [4,5,0,1,2,3]
      mid = (l+r)//2
      res = min(res,nums[mid])
      print("min", res)
      if nums[mid] >= nums[l]:
          l= mid+1
      else:
          r= mid -1
    return res

          
print(findMinOther([4,5,0,1,2,3]))

print("end to end encrpt")