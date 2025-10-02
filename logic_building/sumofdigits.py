# Given a positive number n. Find the sum of all the digits of n.

# 
# Examples:

# Input: n = 687
# Output: 21
# Explanation: Sum of 687's digits: 6 + 8 + 7 = 21
# Input: n = 12
# Output 3
# Explanation: Sum of 12's digits: 1 + 2 = 3


# ********************************************************************
#                   DIGIT EXTRACTION
# ********************************************************************



class Solution:
    def sumOfDigits(self, n):
        # code here
        sum = 0 
        while n != 0 :
            last =  n % 10
            sum+=last
            
            # deelete the last number 
            n//=10
            
        return sum      
            

# ********************************************************************
# [Approach 2] String Conversion

# ********************************************************************



class Solution:
    def sumOfDigits(self, n):
        # code here
        n = str(n)
        sum  = 0 
        for i in n:
            sum+= int(i)
        return (sum) 
s = Solution()
print(s.sumOfDigits(123))







# ********************************************************************
# [Approach 3] recursion 
# ********************************************************************






class Solution:
    def sumOfDigits(self, n):
        if n == 0:
            return 0

        return n%10 + self.sumOfDigits(n//10)
    # 3 + 2 +1
    

s = Solution()
print(s.sumOfDigits(123))
