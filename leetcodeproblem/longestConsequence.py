def consequetiveSequence(arr):
    # Input: nums = [2,20,4,10,3,4,5]
    arr2=arr
    arr2.sort()
    con_arr = [arr2[0]]
    prev =arr2[0]
    for ch in range(1,len(arr2)):
        conSequence = prev +1
        if conSequence == arr2[ch]:
           con_arr.append(arr2[ch]) 
        prev =arr2[ch]

    return len(con_arr)

# print(consequetiveSequence([40,1,2,8,5,34,3,4]))

        

#  optimize way to solve this 



def conseSequenceOptimize(arr):
    setter = set(arr)
    print(setter)
    seq_start = 0
    count = 0 
    for i in setter:
        exits = i-1
        if not exits in setter:
            seq_start = i
            print('start sequence',seq_start) 
            break
    count+=1

    previos = seq_start
    while previos+1 in setter:
        previos+=1
        count+=1
    return count

# print(conseSequenceOptimize([100, 4, 200, 1, 3, 2]))



# *********************************************************************************
#                            More optimiize way
# **********************************************************************************


# def conseSequenceOptimize1(arr):
#     setter = set(arr)
#     print(setter)
#     longest = 0 
#     for i in setter:
#         count = 0 
#         exits = i-1 
#         if not exits in setter:
#             seq_start = i
#             print('start sequence',seq_start) 
#             count+=1

#             previos = seq_start
#             while previos+1 in setter:
#                 previos+=1
#                 count+=1
#             longest = max(longest,count)
#     return longest
            
# print(conseSequenceOptimize1([100,4, 200, 1, 3, 2]))



# quqestion 2

def longestOptimize(arr):
    # [100,4, 200, 1, 3, 2]
    longest = 0
    hash_table = set(arr)
    for num in hash_table:
        count=0 
        if num-1 not in hash_table:
           start_squc = num
           count+=1 
           
           while start_squc+1 in hash_table:
               start_squc+=1
               count+=1

           longest = max(longest,count) 
    return longest           
            
                    
print(longestOptimize([100,2,3,1,5,4]))
