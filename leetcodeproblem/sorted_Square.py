def sortedSquares(nums):
        #   [-4,-1,0,3,10]
        #   [0,1,9,16,100]
        l = 0 
        r = len(nums)-1
        res = []
        while l <= r :
            pow_l = nums[l]**2
            pow_r = nums[r]**2

            if pow_l > pow_r:
               res.append(pow_l)
               l+=1
            else:
                 res.append(pow_r)
                 r-=1

        return res[::-1]

print(sortedSquares( [-4,-1,0,3,10]))   