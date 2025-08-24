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
    
print(encode(arr1))         
    
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
print(decode('4#need5#c#ode'))






