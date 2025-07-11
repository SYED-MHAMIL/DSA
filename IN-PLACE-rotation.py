# To rotate a list k times to the right in-place with O(1) space, you can use the reverse-based algorithm. This avoids using extra memory and works in linear time.

# ✅ Algorithm (Three-Step Reversal):
# Reverse the whole list    --->    done
# Reverse the first k elements
# Reverse the remaining n - k elements

# 🧠 Example:
# arr = [1, 2, 3, 4, 5, 6, 7]
# k = 3
#  step1: [7,6,5,4,3,2,1]
#  step2:  [5,6,7,4,3,2,1]
#  step3:  [5,6,7,4,1,2,3]
   



# def reverse(arr,k):
#     n = len(arr)
#     k =k%n
#     def rotate(start,end):
#         # [1,2,3,4,5,6]
#         # 
#         # stp1 : [6,5,4,3,2,1]
#         # stp2 : [4,5,6,3,2,1]
#         while start <end: # strt:0,1,2,3     end:5,4,3,2
#             arr[start],arr[end] = arr[end],arr[start]
#             start+=1
#             end-=1

#     rotate(0,n-1)
#     rotate(0,k-1)
#     rotate(k+1,n-1)
#     print(f' new arry reverse : {arr}')
    
# reverse([1,2,3,4,5,6],3)


def in_palac_rotation(arr,k):
    n=len(arr)
    k =k%n
    def rotater(start,end):
        #[1,2,3,4,5,6,7] ----> [5,6,7,1,2,3,4]
        #[5,6,7,4,1,2,3]
        #[5,6,7,4,3,2,1]
        #[5,6,7,1,2,3,4]
        while start>end:
                print(arr[-3])
                arr[end],arr[start] =arr[start],arr[end]
                start+=1
                end-=1

    rotater(0,-k)
    return arr
            
    

print(in_palac_rotation([1,2,3,4,5,6,7],3))

# just  reverse


# def rotate_right(arr, k):
#     n = len(arr)
#     k = k % n  # handle k > n
#     # [1,2,3,4,5,6,7] [7,6,5,4,3,2,1]
#     def reverse(start, end):
#         while start < end: # start 0,1,2  or end:6,5,4
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1

#     reverse(0, n - 1)        # Reverse entire list
#     reverse(0, k - 1)        # Reverse first k elements
#     reverse(k, n - 1)        # Reverse the rest
#     return arr

# print(rotate_right([1,2,3,4,5,6,7],3))




# =================    first step    =======================
# =================                  ======================


# def reverse(arr):
#     n=len(arr)
#     start_index = 0
#     end_index=n-1
#     while start_index < end_index:
#         arr[start_index],arr[end_index] = arr[end_index],arr[start_index]
#         start_index+=1 
#         end_index-=1    

#     print(f'array : {arr}')        

# reverse([1,2,3,4,5,6])







# =================    second step    =======================
# =================                  ======================

 


# def reverse(arr,k):
#     n=len(arr)
#     k= k%n  # handle k bara n ho lenth
#     def rotate(start_index,end_index):  # 0 ,-1
#         while start_index < end_index:
#             # [6,5,4,3,2,1]
#             # [4,5,6,3,2,1]
            
#             arr[start_index],arr[end_index] = arr[end_index],arr[start_index]
#             start_index+=1 
#             end_index-=1    
#     rotate(0,n-1) # reverse
#     rotate(0,k-1) # reverse
#     # rotate(k,k+2) # reverse this maybe occur error
#     rotate(k,n-1) # reverse
    

    
#     print(f'array : {arr}')       

# reverse([1,2,3,4,5,6,7],4)






# ===============================   SECOND METHOD ======================


