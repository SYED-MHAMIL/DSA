# # +++++++++++++++++++++++++++++++++++++++++++++++++
#             # brute force way 
# # +++++++++++++++++++++++++++++++++++++++++++++++++
# def constain_duplicate(arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] == arr[j] :
#                return True
#     return False


# print(constain_duplicate([1,3,4,3]))




# +++++++++++++++++++++++++++++++++++++++++++++++++
            # Sorting Method  - - -- - - - 
# +++++++++++++++++++++++++++++++++++++++++++++++++
# def constain_duplicate(arr):
#     sorted_array = arr[::]
#     sorted_array.sort()
#     for i in range(len(sorted_array)):
#        if count:=sorted_array.count(sorted_array[i]) >=2:
#            return True 
#     return False


# print(constain_duplicate([3,3]))


# def contain_duplicate(arr):
#     arr.sort()
#     for i in range(len(arr)-1):
#         if arr[i] == arr[i+1]:
#             return  True
        
#     return False

# print(contain_duplicate([4,3,2,5]))








# +++++++++++++++++++++++++++++++++++++++++++++++++
            # Through hash set Method  - - -- - - - 
# +++++++++++++++++++++++++++++++++++++++++++++++++

def contain_duplicate(arr):
    hash_set = set()
    for i in range(len(arr)):
        if arr[i] in hash_set:
           return True
        else:
            hash_set.add(arr[i]) 
    return False


print(contain_duplicate([1,3,56]))




def contain_duplicate(arr):
    sete= set()
    return len(set(arr)) != len(arr)

print(contain_duplicate([1,3,4,5])) 