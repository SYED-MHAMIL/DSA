
def longestKSubstr(s, k):
    # code here
#   first step will be take out the length
#  second we will make the varibale  that take the longest substring
#  we will put it there loop  for 
    n = len(s)
    res = -1
    
    for l in range(n):
        obj={}
        for r in range(l,n):
            # print(r)
            obj[r] = obj.get(r,0)+1
            if len(obj) == k:
                res = max(res,r-l+1)
                print("REs" ,res)
            elif len(obj) > k:
                break
            
    return  -1 if (res < k) else  res

print(longestKSubstr("aabacbebebe",3))