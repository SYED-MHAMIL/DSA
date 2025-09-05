
# def encode( strs):
#     encode_str = ''
#     for i in strs:
#         encode_str += str(len(i))+'#'+ i 
#     return encode_str


# def decode(s) :
#     decode_arr = []
#     i= 0
#     # str  = '4#need5#cod#e' 
#     while i<len(s):
#         j =i
#         while s[j] != '#':
#                 j+=1
#         index= int(s[i:j])
#         decode_arr.append(s[j+1:index+j+1])
#         # print(decode_arr)
#         i = index+j+1
        
#     return decode_arr



    
# # print(encode(["neet","code","love","you"]))
# print(decode('4#neet4#code4#love3#you'))





def encode( strs):
    encode_word = ':;'.join(strs)
    return encode_word



def decode(s) :
    decode_arr = []
    i= 0
    # str  = 'neet:;code:;love:;you' 
    while i<len(s):
        j =i 
        while j  < len(s) and s[j] != ';':
            if  j < len(s):
                j+=1
        slice_str =s[i:j]
        if(':'in slice_str):
          decode_arr.append(s[i:j-1])
        else:
            decode_arr.append(slice_str)

        
        i = j+1
    return decode_arr
        
# print(encode(["neet","code","love","you"]))
print(decode('neet:;code:;love:;you'))

