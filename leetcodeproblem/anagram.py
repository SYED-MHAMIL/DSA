from operator import add
import string 
# ============================================
#          Brute Force ---> method
# ============================================


# def checkAnagram(s,t):
#     # Input: s = "racecar", t = "carrace"
#     sorted_s = sorted(s)
#     sorted_t= sorted(t)
#     return  sorted_s == sorted_t

# print(checkAnagram('abc','cha'))

       


# ============================================
#          like hash method ---> method
# ============================================
from functools import reduce

def checkAnagramSet(s,t):
    if len(s) != len(t):
       return False
    # Input: s = "racecar", t = "carrace"

    k= string.ascii_lowercase
    p={i:0 for i in k}
   
  
    for ch in s:
        if ch in p:
            p[ch] += 1
    for ch in t:
        if ch in p:
              p[ch] -= 1
    print('\n after',p)
    return reduce(lambda acc,ch:acc+abs(ch),p.values()) ==0 
# print(checkAnagramSet('asc','cba'))





# ============================= =========================
#           hash map method ---> method
# =================================================



# def checkAnagram(s,t):
#    if len(s) != len(t):
#       return False   
#    count_S, count_T = {}, {}
#    # s= aad, t= daa
#    for i in range(len(s)):
#       count_S[s[i]] = 1 + count_S.get(s[i],0)
#       count_T[t[i]] =1 +count_T.get(t[i],0) 
#    print('firsts', count_S)
#    print('Second count', count_T)

#    return   count_S == count_T

# print(checkAnagram('aad','daa'))






# ============================= =========================
#          Through array list ---> method
# =================================================

# def anagram(s,t):
#     if len(s) != len(t):
#        return False
#     # s= 'aab'   ,  t = 'cba'
#     arr = [0]*26
#     for i in range(len(s)):
#         arr[ord(s[i]) - ord('a')]+=1
#         arr[ord(t[i]) - ord('a')]-=1 
    
#     for i in arr:
#         if i != 0:
#           return False
#     return True         

# print(anagram('aab','aab'))