# Given an Integer n, find the reverse of its digits.

# Examples:  

# Input: n = 122
# Output: 221
# Explanation: By reversing the digits of number, number will change into 221.

# Input: n = 200
# Output: 2
# Explanation: By reversing the digits of number, number will change into 2.

# Input: n = 12345 
# Output: 54321
# Explanation: By reversing the digits of number, number will change into 54321.



def reverse_digit(n):
    rev= 0 
   
    while n != 0:
        # 123
        # 321
        last = n%10
        rev= rev* 10 + last
        n= n//10
    return rev  


print(reverse_digit(123))



print("\n ******************************************************* \n")
print("\n ******************************************************* \n")


def reverse_digit(n):
    rev= "" 
   
    while n != 0:
        # 123
        # 321
        last = n%10
        rev+= str(last)
        n= n//10
    return int(rev)  


print(reverse_digit(123))


print("\n ******************************************************* \n")
print("\n ******************************************************* \n")


def reverse_digit(n):
    rev= "" 
    n = str(n) 
    for i in range(len(n)-1,-1,-1):
        rev+=n[i]
        # print(i)
    return int(rev)
   
    
print(reverse_digit(123))

print("\n ******************  Third Way to FRom recursiton  ****************** \n")


def reverse_digit(n):
    if n ==0:
        return 0 
    last = n%10
    rev = reverse_digit(n//10)
    return rev*10 +last   
    
print(reverse_digit(123))
