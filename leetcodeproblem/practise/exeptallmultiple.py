    # most optimize way

# nums = [1,2,3,4]
def exceptAllmultiple(str_Arr):
    res=  [0]*len(str_Arr)
    res2=[0]*len(str_Arr)
    suffix,prefix =  1,1     
    for i in  range(len(str_Arr)):
        res[i]=suffix
        suffix*=str_Arr[i]
    # [1,1,2,6]
    
    for i in  range(len(str_Arr)-1,-1,-1):
        res2[i]=prefix
        prefix*=str_Arr[i]
    result= []
    for i in range(len(res)):
        result.append(res[i]*res2[i])             
    return result
# print(exceptAllmultiple([1,2,4,6]))







# another more optimal 


def exceptAllmultiple1(str_Arr):
    #  input =  [1,2,4,6]
    
    res=  [0]*len(str_Arr)
    
    suffix,prefix =  1,1     
    for i in  range(len(str_Arr)):
        res[i]=suffix
        suffix*=str_Arr[i]
    # [1,1,2,6]
    for i in  range(len(str_Arr)-1,-1,-1):
        res[i]*=prefix
        prefix*=str_Arr[i]
    return res

print(exceptAllmultiple1([1,2,4,6]))




