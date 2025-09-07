from collections import OrderedDict 
# from through can be done for remove duplicate



# ****************************************************************
                #  Brute Force way 
# ****************************************************************

def longestwithBrute(strs):
    max_val = 0
   # Input: strs = "zxzzxyz"
    for i in range(len(strs)):
        hash = set()
        for j in range(i,len(strs)):
            if  strs[j] in hash:
                break
            hash.add(strs[j]) 
        max_val =max(max_val,len(hash))
    return max_val

# print(longestwithBrute('geeksforgeeks'))        

            


# ****************************************************************
                # optimized  way 
# ****************************************************************



# def longestwithPoint(strs):
#     # strs =  pwwkew
#     max_val = 0
#     hash_chr = set()
#     l =0 
#     for i in range(len(strs)):
#         while strs[i] in hash_chr:
#             hash_chr.remove(strs[l])
#             l+=1
#         hash_chr.add(strs[i])
#         max_val = max(max_val,len(hash_chr))  
    
#     return max_val

# print(longestwithPoint('geekee'))






def longestwithPoint2(strs):
    res= set()
    max_len = 0
    l =0 
    for i in range(len(strs)):
        while strs[i] in res:
            res.remove(strs[l])        
            l+=1
        res.add(strs[i])
        max_len = max(max_len,len(res))

    return max_len

print(longestwithPoint2('geekee'))