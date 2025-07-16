#  ===================    FIrst version

# list_xors = [[3,400,5],[5,6,7],[45,54,23]]
# Which_max= []
# for listX in list_xors:
#     xor_val = 0 
#     for v in listX:
#         xor_val^=v

#     Which_max.append((xor_val,listX))

# p= max(Which_max,key=lambda x:x[0],default=None)
# if p:
#     print(p[1])
# else:
#     print("no sublists found")



from functools import reduce
list_xors = [[3,4,5],[5,6,7],[45,54,23]]
# reduce(function, iterable, initializer=None)


max_xor= max(( reduce(lambda x,y:x^y,lis),lis) for lis in list_xors)
print(max_xor[1])
