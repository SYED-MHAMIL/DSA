# bruete forrce

def duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
               return True
    return False
# print(duplicate([1,3,3,4,5,5]))
            




#  hash map 

def duplicate1(arr):
    obj = set()
    for i in range(len(arr)):
        if arr[i] in obj:
           return True
        else:
            obj.add(arr[i])

     
    return False
print(duplicate1([1,3,3,4,5,5]))
            

