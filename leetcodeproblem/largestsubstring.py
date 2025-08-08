# **********************************************************
#       Bruce force approach with time complexity O(2)
# **********************************************************





def is_dup(string):
    counter = 0
    max_val =0
    for i in range(len(string)):
        counter = string.count(string[i])
        max_val =max(max_val,counter)
    if max_val<=1:
        return True
    else:
         return False


print(is_dup('abc'))
          

def lengthOfLongestSubstring( s: str) -> int:
        res = []
        max_len=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                sub_string =s[i:j+1]
                if is_dup(sub_string) :
                   res.append(sub_string)
        # print(res)
        for substring_num in res:     
            max_len = max(max_len,len(substring_num))
        return max_len

print(lengthOfLongestSubstring("abcd"))




