# **********************************************************
#       Bruce force approach with time complexity O(2)
# **********************************************************





class Solution:
    def groupAnagrams(self, strs ):
        arr = []
        # Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
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
        sorted_v = "".join(sorted(strs[i]))
        # exists = any(sorted_v in ar for ar in arr)
        idx=next((i for i,g in enumerate(arr) if ''.join(sorted(g[0])) ==sorted_v  ),-1)

        if idx != -1:
            arr[idx].append(word)
        else:
            arr.append([word])
    return arr
print(groupAnagram(['']))


















