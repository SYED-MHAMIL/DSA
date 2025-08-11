
# +++++++++++++++++++++++++++++++++++++++++++++++
#           BRUTE FORCE WAY
# +++++++++++++++++++++++++++++++++++++++++++++++
# def twoSum(arr,target):

#     # target  =8
#     # arr = [4,5,6,3]  
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if arr[i]+arr[j] == target:
#                index= [i,j]
#                break
#     return index


# print(twoSum([4,5,6,3],8))




# +++++++++++++++++++++++++++++++++++++++++++++++
#           Two pointer  WAY
# +++++++++++++++++++++++++++++++++++++++++++++++



# def twoSum(arr,target):

#     # target  =8
#     # arr = [4,5,6,3]
#     l=0
#     r=0
#     sorted_f = sorted(arr)  
#     sorted_l = sorted(arr,reverse=False)  
#     while True :
#         sumOfTwo =sorted_f[r] + sorted_l[l]
#         if sumOfTwo>target:
#             l+=1
#             sorted_l[l]
#         elif sumOfTwo<target:
#             r+=1
#             sorted_f[r]
#         else:
#             right =arr.index(sorted_f[r])
#             left =arr.index(sorted_l[l])
#             break
#     return [right,left]
            


# print(twoSum([4,5,6,3],8))



# +++++++++++++++++++++++++++++++++++++++++++++++
#           Two pointer  WAY just inhaance code
# +++++++++++++++++++++++++++++++++++++++++++++++


def twoSum(arr, target):
    # store original indices before sorting
    indexed_arr = list(enumerate(arr))
    indexed_arr.sort(key=lambda x: x[1])

    left = 0
    right = len(arr) - 1

    while left < right:
        sum_val = indexed_arr[left][1] + indexed_arr[right][1]
        if sum_val == target:
            
            return [min(indexed_arr[left][0],indexed_arr[right][0]), max(indexed_arr[right][0],indexed_arr[left][0])]
        elif sum_val < target:
            left += 1
        else:
            right -= 1

print(twoSum([4, 5, 6, 3], 8))  # Output: [0, 1]


