# **********************************************************
#       Bruce force approach with time complexity O(2)
# **********************************************************





class Solution:
    def groupAnagrams(self, strs ):
        arr = []
        # Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["   ","tan"],["ate","eat","tea"]]
        for i in range(len(strs)):
            arr2=[]
            
            for j in range(i,len(strs)):
                s =sorted(strs[i])
                t = sorted(strs[j])
                if s == t:
                   exsits = any(strs[j] in g for g in arr)
                   if not exsits :  
                      arr2.append(strs[j])
            if arr2:
               arr.append(arr2)
        return arr
    


# **********************************************************
#                again n2 log because we use sorting
# **********************************************************


def groupAnagram(strs):
    # Input: strs = ["act","pots","tops","cat","stop","hat"]
    arr= []
    for i in range(len(strs)):
        word= strs[i]
        sorted_v = "".join(sorted(word))
        # exists = any(sorted_v in ar for ar in arr)
        idx=next((i for i,g in enumerate(arr) if ''.join(sorted(g[0])) ==sorted_v  ),-1)

        if idx != -1:
            arr[idx].append(word)
        else:
            arr.append([word])
        return arr
# print(groupAnagram(['']))





# **********************************************************
#              by using Hash map usuall that is not hash map 
# **********************************************************

# def groupAnagram(strs):
#     arr = [] 
#     hash_map = {}
#     for i in range(len(strs)):
#         sorted_v = sorted(strs[i])
#         value= strs[i]
#         if sorted_v in hash_map:
#             idx=next((i for i,g in enumerate(arr) if sorted_v in g),-1)
#             if idx != -1:
#                  arr[idx].append([value])
#         else:
#             arr.append([value])
#             hash_map.add(sorted_v)

#     return arr
# # print(groupAnagram(["eat","tea","tan","ate","nat","bat"]))

# from collections import defaultdict

# # def  groupAnagram1(strs):
# print(defaultdict(dict))



# ********************************************************************
#                         *** hash map using default dict 
# *********************************************************************

from collections import defaultdict

dict_str = defaultdict(int)
def anagramAanalyse(strs):
    for i in range(len(strs)):
        sorted_str = ''.join(sorted(strs[i]))
        dict_str[sorted_str].append(strs[i])

    res = list(dict_str.values())
    return res
# print(anagramAanalyse(["eat","tea","tan","ate","nat","bat"]))




# ===========================================================
                #    Build from ai engieer mhamil ali
# ===========================================================





def analysisAnagram(strs):
    dict_str = {}
    for i in range(len(strs)):
        sorted_str =  ''.join(sorted(strs[i]))
        if not dict_str.get(sorted_str,None):
           dict_str[sorted_str] = []
        dict_str[sorted_str].append(strs[i])
    
    return list(dict_str.values())

# print(analysisAnagram(["eat","tea","tan","ate","nat","bat"]))



    
# ===========================================================
                #    Build from ai engieer mhamil ali USING ARAY
# ===========================================================

def analyAnagramsgroup(strs):
    
    dic_str = defaultdict(list)
    # res = []
    for i in strs:
        ch = [0] * 26
        for char in i:
            ch[ord(char)- ord('a')]+=1
        dic_str[tuple(ch)].append(i)

    return list(dic_str.values())    
        

print(analyAnagramsgroup(["eat","tea","tan","ate","nat","bat"]))     
        







        