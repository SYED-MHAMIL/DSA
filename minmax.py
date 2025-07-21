# ***************************************************
#     MIN-MAX
# ***************************************************



# step-1

arr =[2,3,4,12]
arr.sort()  # because i dont know list was before sorted
min =(arr[:-1])
max =(arr[1:])
# print(min,max)


# step#2
#  [1,2,3,4,5]




def miniMaxSum(arr):
    temp= 0
    min =0
    max = 0
    n =len(arr)
    arr.sort()
    for i in range(n):
        temp+=arr[i]
        if i == n-2:
           min+=temp 
        
    max =temp-arr[0]
    print(min,max)    


    
miniMaxSum([2,3,4,1])