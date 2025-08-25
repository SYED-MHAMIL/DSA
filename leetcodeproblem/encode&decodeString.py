# *************************************************************
#          encode & decode  
# *************************************************************

arr1= ['need', 'c#ode']

def encode(str_arr):
    if not str_arr:
        return ''
    res  = ''    
    for arr in str_arr:
        res+= str(len(arr)) + "#" + arr
    return res
    
# print(encode(arr1))         
    
def decode(str_arr):
    # 4#need5#c#ode
    res,i = [],0
    while i < len(str_arr):
        j =i 
        while str_arr[j] != '#':
              j+=1
        length = int(str_arr[i:j])
        res.append(str_arr[j+1 : j+1+ length ])
        i = j+1+ length  
    return res
# print(decode('4#need5#c#ode'))



# practise  


def encode_str(arr):
    res = ''
    for stri in arr:
        res+=(str(len(stri))+'#'+stri)
    return res
print(encode_str(arr1))    


def decode_str(arr_str):
    res,i = [], 0
    # arr= 4#need5#c#ode
    while i < len(arr_str):
        j =  i 
        while arr_str[j] != "#":
              j+=1
        length = int(arr_str[i:j])
        res.append(arr_str[j+1:j+1+length])
        i= j+1+length
    return res

print(decode_str('4#need5#c#ode'))


        
        


         
         