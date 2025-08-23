# ******************************************************
#               Brute force method 
# ********************************************************


def Product_of_element_except_self(arr):
    # arr = [1,2,3,4]
    arr1 = []
    for i in range(len(arr)):
        multiple=1
        for j in range(0,len(arr)):
            if arr[i] != arr[j]:
               multiple*= arr[j]
        arr1.append(multiple)

    return arr1

# print(Product_of_element_except_self([1,2,3,4]))  







# ******************************************************
#               division   method 
# ********************************************************



# but in problem  because when we'll use [-1,1,0,-3,3] in array the answer is wrong
def exceptSelf(arr):
    avg= 1
    for i in arr:
        avg*= i 
    
    res = [] 
    for j in arr:
        res.append(int(avg/j))
    
    return res

# print(exceptSelf([1,2,3,4])) # change from [-1,1,0,-3,3]       


def product_all_exceptSelf(arr):
    avg,zero_count = 1 ,0
    # arr =  [-1,1,0,-3,3]
    for num in arr:
        if num:
           avg*= num
        else:
            zero_count+=1

    if zero_count > 1: return [0] * len(arr)
    res=  [0] * len(arr)
    for i,v in enumerate(arr) :
        if zero_count:res[i] =0 if v else avg 
        else: res[i] = avg//v 

    return res


# print(product_all_exceptSelf([1,0,4,5,4,5]))
# 













# *****************************************************************
                # second optimize way                                         
#*****************************************************************




def p_ELement_except_self(arr):
    # arr = [1,2,3,4]
    #   pref =[1 ,1, 2,6]
    #   suff =[24,12,4,1]
    n = len(arr)
    res= [0] * n
    suff = [0] * n
    pre = [0] * n

    pre[0] = suff[n-1] = 1
    for i in range(1,n):
        pre[i]= arr[i-1] * pre[i-1]

    for j in range(n-2,-1,-1):
        suff[j] =arr[j+1] * suff[j+1]

    for k in range(n):
        res[k] = pre[k]* suff[k]
    
    return res

print('pre, suff',p_ELement_except_self([1,2,3,4]))




# ******************************************************
#              most OPtimize way to solve this question  O(n)
# ********************************************************

# from operator import mul
def Product_of_element_except_self1(arr):
    res= []
    for i in range(len(arr)):
        left= arr[0:i]
        right = arr[i+1:]

        left_m = 1
        for k in left:
            left_m*=k

        right_m = 1
        for j in right:
            right_m*=j
        print(left_m)
        print(right_m)
        
        res.append(left_m *right_m)
        
    print(res)    
        
         

# Product_of_element_except_self1([-1,1,0,-3,3])





def productExceptSelf(nums):
        # [1 , 2 , 3 , 4]
    res= [0] * len(nums)    
    prefix =1
    for i in range(len(nums)):
        res[i]=prefix
        prefix*=nums[i]
    
    postfix =1
    for i in range(len(nums)-1 ,-1, -1):
        res[i] *= postfix
        postfix  *= nums[i]
        
    return res



print(productExceptSelf([3434,45*4645645645645,0,4]))