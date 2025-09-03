### ____________________________group anagram____________________________________


strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
def groupAnangram(strs):
    arr= []
    for i in range(len(strs)):
        arr2=[]
        for j in range(len(strs)):
            sortedarr= sorted(strs[i])
            sortedarr2=sorted(strs[j])
            if sortedarr == sortedarr2:
                exists = any( strs[j]  in iterate  for iterate in arr)
                if not exists:
                   arr2.append(strs[j])
        if arr2:
                arr.append(arr2)       
    return arr
            

# print(groupAnangram(strs))



# use another method 


def groupAnagraUsingNext(strs_Arr):
    arr = [] # 
    for i in range(len(strs_Arr)):
            sorted_v= ''.join(sorted(strs_Arr[i]))
            idx = next((index for index,k in enumerate(arr) if "".join(sorted(k[0])) == sorted_v),-1)
            if idx != -1:
               arr[idx].append(strs_Arr[i])
            else:
                arr.append([strs_Arr[i]])

    return arr 
# print(groupAnagraUsingNext(["act","pots","tops","cat","stop","tac"]))
        
            



# using default dict

from collections import defaultdict
def groupAnagraUsingdefaultDic(strs_Arr):
    defdic = defaultdict(list)
    for i in range(len(strs_Arr)):
            sorted_v= ''.join(sorted(strs_Arr[i]))
            defdic[sorted_v].append(strs_Arr[i])
            
    return list(defdic.values()) 
# print(groupAnagraUsingdefaultDic(["act","pots","tops","cat","stop","hac"]))



def groupAnagraUsingDic(strs_Arr):
    defdic = {}
    for i in range(len(strs_Arr)):
            sorted_v= ''.join(sorted(strs_Arr[i]))
            if defdic.get(sorted_v):
              defdic[sorted_v].append(strs_Arr[i])
            else:
                 defdic[sorted_v] = [strs_Arr[i]]
                 
            
    return list(defdic.values()) 
# print(groupAnagraUsingDic(["act","pots","tops","cat","stop","hac"]))




# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                Most optimize way
# ++++++++++++++ +++++++++++ ++++++++++ +++++++++++++++++++++++++++++++++++++++++++++++++++++++





def groupAnagraUsingoptimizeAWay(strs_Arr):
    defdic = {}
    for i in range(len(strs_Arr)):
        ch = [0] *24

        for char in strs_Arr[i]:
            ch[ord(char) - ord('a')] += 1

        if defdic.get(tuple(ch)):
            defdic[tuple(ch)].append(strs_Arr[i])
        else:
                defdic[tuple(ch)] = [strs_Arr[i]]
                
            
    return list(defdic.values())

# print(groupAnagraUsingoptimizeAWay(strs_Arr=strs))






# def groupAnagraUsingoptimizeAWay(strs_Arr):
#     objDefault = {}
#     for word in strs_Arr:
#         ch = [0] * 26
#         for chr in word:
#             if  
        
# print(groupAnagraUsingoptimizeAWay(strs_Arr=strs))






