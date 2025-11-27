def countTriplets(n,sum,arrs):
        arr = sorted(arrs)
        #code here
        ans = 0 
        for i in range(n-2):
            l = i+1
            r = n - 1
            
            while l < r :  
                sum_up = arr[i]+arr[l]+arr[r] 
                if sum_up <sum:
                   l+=1
                else:
                   r-=1 
        return  ans


s = countTriplets(4,2,[-2, 0, 1, 3])
# print(s)