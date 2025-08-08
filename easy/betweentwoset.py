import math
from functools import reduce

# # LCM of array
# def lcm(a):
#     return reduce(lambda x, y: x * y // math.gcd(x, y), a)

# # GCD of array
# def gcd(b):
#     return reduce(math.gcd, b)


# def getTotalX(a,b):
#         l=lcm(a)
#         g=gcd(b)
#         print("gcd --->",g)
#         print("lcm --->",l)
#         count =0
#         multiple =l 
#         while multiple <=g:
#              if g%multiple == 0:
#                   count+=1
#              multiple+=l
            
#         return count      


# print("answer -->",getTotalX([2,5],[16, 32, 96]))
             
# print(math.lcm(2,5)//math.gcd(2,5))




def lcm(a):
    return reduce(lambda x,y:(x,y)//math.gcd(x,y),a)
    
def gcd(b):
    return reduce(math.gcd,b)

    

def getTotalX(a,b):
    l =lcm(a)
    g= gcd(b)
    
    
    count = 0 
    multiple = l
    while multiple<=g:
        if g%multiple == 0 :
            count+=1
        multiple+=l
        
    return count     
    

print(getTotalX([2,4],[16,32,96]))