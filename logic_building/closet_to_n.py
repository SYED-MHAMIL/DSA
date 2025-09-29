#     Find Closest to n and Divisible by m
# Last Updated : 09 Jul, 2025
# Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

# Examples: 

# Input: n = 13, m = 4
# Output: 12
# Explanation: 12 is the closest to 13, divisible by 4.

# Input: n = -15, m = 6
# Output: -18
# Explanation: Both -12 and -18 are closest to -15, but -18 has the maximum absolute value.



def closestNumber(n, m):
        
        # code here
       closest = 0
       min_difference = float('inf')

       for i in range(n-abs(m),n+abs(m)+1):
           if i%m == 0:
              diff = abs(n-i)
              if  diff <  min_difference or ( diff  == min_difference and abs(i)> abs(closest)):
                  closest = i
                  min_difference =diff
              
       return closest

print(closestNumber(-15,6))


# print(-18%6)




# for i in range(-21,-9+1):
#     print(i)

