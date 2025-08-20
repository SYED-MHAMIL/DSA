# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

    # 1 <= nums.length <= 10^4.
    # -1000 <= nums[i] <= 1000
    # 1 <= k <= number of distinct elements in nums.




# ***************************************************************
#                Sorting
# ***************************************************************




# def k_frequency(arr,k):
# # Input: nums = [1,2,2,3,3,3], k = 2
     
#     #  arr =[]
#     obj = {}
#     for i in range(len(arr)):
#         obj[arr[i]]= obj.get(arr[i],0) +1 

#     sorted_arr = [key for key,val in sorted(obj.items(),reverse=True,key=lambda x:x[1])][:k]
#     return sorted_arr

# k_frequency([1,2,2,4,4,3,3,3],k = 2)     


# **************************************************************
#          all kth element
# **************************************************************


def kthFreqby_sorting(arr,k):
    # arr = 1,1,2,2,3,3,3,5,5,7,7,7
    obj = {}
    for i in arr:
        obj[i] =1 + obj.get(i,0) 

    sorted_item =sorted(obj.items(),key=lambda x:(-x[1],x[0]))
    
    if len(arr) <k:
       return [x for x,y in sorted_item] 
    print(obj)
    print(sorted_item)

    kth_freq = sorted_item[k-1][1]
    return [x for x,f in sorted_item if f>=kth_freq ] 


    # print(sorted_item)

# print(kthFreqby_sorting([1,1,2,2,3,3,3,5,5,7,7,7],4))

    









def k_frequency(arr,k):
# Input: nums = [1,2,2,3,3,3], k = 2
     
    #  arr =[]
    obj = {}
    for i in range(len(arr)):
        obj[arr[i]]= obj.get(arr[i],0) +1 

    # sorted_arr = [key for key,val in sorted(obj.items(),reverse=True,key=lambda x:x[1])][:k]
    sorted_items = sorted(obj.items(), key=lambda x: (-x[1], x[0]))
    
    #  if kth grather than sorted_items in that case we will return whole list 
    if k >len(sorted_items):
           return [ num for num,v in sorted_items]
    print(sorted_items)
    kth_freq =sorted_items[k-1][1]
    return [num for num,f in sorted_items if f >= kth_freq]
    
# print(k_frequency([1,2,2,4,4,3,3,3,5,5,5,8,8,8,8],3)) 




# ***************************************************************
#          +++++++++++++    min-heap    +++++++++
# ***************************************************************


import heapq

def frequent_kth_element(arr,k):
    # arr = 1,1,3,3,3,5,5,7,7
    obj = {}
    for i in arr:
        obj[i] = obj.get(arr[i],0) +1
    
    heap = []
    for key in obj.keys():
        heapq.heappush(heap,(obj[key],key))
        if len(heap) > k:
           heapq.heappop(heap)
        
    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])
        
    return res
               
# print(frequent_kth_element([1,1,3,3,3,5,5,7,7],2))


# ****************************************************
 #        kth freqncy  uing min heap  
# ****************************************************

def kth_freq_minheap(arr,k):

    obj= {}
    for i in arr:
        obj[i] =1+ obj.get(i,0)
    
    sorted_items = sorted(obj.items(), key=lambda x: (-x[1], x[0]))
    heap = []

    for num,f in sorted_items:
        kth = sorted_items[k-1][1]
        heapq.heappush(heap,(f,num))
        print('heap',heap)
        if len(heap) > k:
           heapq.heappop(heap)
    return [number for fr,number in heap]
# print(kth_freq_minheap([1,2,2,8,8,8,4,4],2))    



import heapq

def kth_freq_minheap(arr, k):
    obj = {}
    for i in arr:
        obj[i] = 1 + obj.get(i, 0)
    
    heap = []
    for num, f in obj.items():
        heapq.heappush(heap, (f, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # The kth largest frequency = smallest freq in heap now
    kth_freq = heap[0][0]
    print(heap)

    # Collect all numbers with freq >= kth_freq
    result = [num for num, f in obj.items() if f >= kth_freq]
    return result

print(kth_freq_minheap([1,2,2,8,8,8,4,4,9,9], 2))











# ***************************************************************
#     ++++++++++    optimize way- bucket solution    +++++++++
# ***************************************************************

# def freq_kth_element(arr,k):
#     obj = {}
#     freq= [[] for i in range(len(arr)+1)]
#     for i in arr:
#        obj[i] = obj.get(i,0)+1

#     for num,v in obj.items():
#         freq[v].append(num)
#     res = []
#     for i in range(len(freq) - 1, 0, -1):
#         for num in freq[i]: 
#             res.append(num)
#             if len(res) == k:
#                 return res
#     return res
        
# print(freq_kth_element([1,1,3,3,3,5,5,7,7],2))

         

# [[1],[2,3,4]]






# ***************************************************************
#     ++++++++++    optimize way- bucket solution BOTH WAY CORRECT    +++++++++
# ***************************************************************






def freq_kth2_element(arr,k):
    obj = {}
    for i in arr:
        obj[i] = obj.get(i,0) +1

    bucket = [[] for _ in range(len(arr) +1)]    
    for nums,f in obj.items():
        bucket[f].append(nums)
    
    res = []
    for j in range(len(arr)-1, 0 , -1):
        for num in bucket[j]:
            res.append(num)
        if len(res) >= k :
            break
    
    return res 

        


    # print(bucket)    
# print(freq_kth2_element([1,1,3,3,3,5,5,7,7,8,9],2))

         

