#Find Closest to n and Divisible by m
# Last Updated : 09 Jul, 2025
# Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

# Examples: 

# Input: n = 13, m = 4
# Output: 12
# Explanation: 12 is the closest to 13, divisible by 4.

# 13-4 = 9
# diff = 16-13 = abs (1)
# diff < prevdiff :
#    closet =12






# Input: n = -15, m = 6
# Output: -18
# Explanation: Both -12 and -18 are closest to -15, but -18 has the maximum absolute value.


# -15-6= -21
# -15+6= -9
# -15 -(-12)
# -15-(-18)

# if diff same but closet should be greather previous one 


def  closestFind(n,m):
    closest  = 0 
    min_diff= float('inf')
    
    for i in range(n-abs(m),n):
        if i%m == 0:
          diff = abs(n-i)
          if diff < min_diff or (diff == min_diff and  abs(i)>  abs(closest)):
             min_diff = diff
             closest =  i  
     
    print('\noutput:')
    return closest
        
# print(closestFind(13,4))





def closestNumber(n, m) :
    q = int(n/m)
    # lets  -15/6 = -2
    n1 =  q * m
    #  n1 =  -12

    # if (n*m) > 0:
    #    n2= m *(q+1)
    # else:
    if n <0:
        n2= m *(q-1)
        # -18
    
    if abs(n-n1) < abs(n-n2):
       return n1


    return n2
    
if __name__ == "__main__":
  n = -15; m = 6
  print(closestNumber(n, m))








# def closestNumber(n, m):
        
#         # code here
#        closest = 0
#        min_difference = float('inf')

#        for i in range(n-abs(m),n+abs(m)+1):
#            if i%m == 0:
#               diff = abs(n-i)
#               if  diff <  min_difference or ( diff  == min_difference and abs(i)> abs(closest)):
#                   closest = i
#                   min_difference =diff
              
#        return closest

# print(closestNumber(-15,6))


# # print(-18%6)




# # for i in range(-21,-9+1):
# #     print(i)

