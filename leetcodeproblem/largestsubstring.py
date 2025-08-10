# **********************************************************
#       Bruce force approach with time complexity O(2)
# **********************************************************





# def is_dup(string):
#     counter = 0
#     max_val =0
#     for i in range(len(string)):
#         counter = string.count(string[i])
#         max_val =max(max_val,counter)
#     if max_val<=1:
#         return True
#     else:
#          return False


# print(is_dup('abc'))
          

# def lengthOfLongestSubstring( s: str) -> int:
#         res = []
#         max_len=0
#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                 sub_string =s[i:j+1]
#                 if is_dup(sub_string) :
#                    res.append(sub_string)
#         # print(res)
#         for substring_num in res:     
#             max_len = max(max_len,len(substring_num))
#         return max_len

# print(lengthOfLongestSubstring("aabddcd"))



# +++++++++++++++++++++++++++++++
        #    another way but prolem is that we have just time sbstring without dp
# +++++++++++++++++++++++++++++++


# class Solution:
def lengthOfLongestSubstring(s: str) -> int:
        res =0
        for i in range(len(s)):
            charac =set() # a
            for j in range(i,len(s)):
                if not s[j] in charac:
                    charac.add(s[j])
            res = max(res,len(charac))
            # break  # you can also in one step 
        return res
                
        
    
# print(lengthOfLongestSubstring("aabddcd"))




# +++++++++++++++      ++++++++++++++++
#        another way Correct way/ shrt answer but O(n2)
# +++++++        ++++++++++++++++++++++++



def longeST_CAHR(s):
    # aabddcd
    res =0 
    for i in range(len(s)):
        rep =set() 
        for j in range(i,len(s)):
            if s[j] in rep:
                break
            rep.add(s[j])
        res = max(res,len(rep))
    return res

# print(longeST_CAHR("pwwk"))



# **********************************************************
#               SLIDING(2 point approach)   WINDOW     O(n)
# **********************************************************



def pointer_method(s):
    # s = pwwwrst
    l =0 
    res=0 
    charSet = set()
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1        

        charSet.add(s[r])
        res = max(res,len(charSet))
        
    return res
# print(pointer_method("pwwwrst"))

# def pointer_method(s):
#     # s = "pwwk"
#     charSet= set()
#     res =0
#     l=0 
#     for i in range(len(s)):
#         while s[i] in charSet:
#              charSet.remove(s[l])
#              l+=1
                           
#         charSet.add(s[i])
#         res = max(res,len(charSet))
#     return res
# print(pointer_method("pwwk"))





# ***************************************
#    sliding window (optimaL Way )
#******************************************


def lenghtoflargestsubsstring(s):
    l=0
    res =0 
    obj = {}
#   s ='abbbcd'
    for r in range(len(s)):
        if s[r] in obj:
            l = max(obj[s[r]]+1,l)
        obj[s[r]]= r   
        res = max(res,r-l+1)

    return res

print(lenghtoflargestsubsstring("abbbcd"))