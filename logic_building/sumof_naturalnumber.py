# Input: n = 3
# Output: 6
# Explanation: 1 + 2 + 3 = 6

# Input: n = 5
# Output: 15 
# Explanation:  1 + 2 + 3 + 4 + 5 = 15



# ans through  recursion method  

def sum_of_natutal(n):
    if n == 0:
        return 0 
    return n + sum_of_natutal(n-1   )
print(sum_of_natutal(5))

# 5+4+3+2+1+0






# question 
# Input : n = 2
# Output: 5
# Explanation: 1^2+2^2 = 5

# Input : n = 8
# Output: 204
# Explanation :  1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 = 204 


def summation(n):
    if n == 1:
       return 1
    
    return  n*n + summation(n-1)

print(summation(8))



