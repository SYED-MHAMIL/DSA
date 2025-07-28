    # n = int(input().strip())

# genes = input().rstrip().split()
genes =['a','b','c','aa','d','b']
# health = list(map(int, input().rstrip().split()))
health = [1,2,3,4,5,6]
# s = int(input().strip())
s= 3
for s_itr in range(1):
    # first_multiple_input = input().rstrip().split()
    first_multiple_input=[1,5,"caaab"]
    first = int(first_multiple_input[0])
    last = int(first_multiple_input[1])
    d = first_multiple_input[2]
    gen1=genes[first:last+1]
    hel1= health[first:last+1]
    print(gen1)
    print(hel1)
    print(d)
    
    
    for i,v in enumerate(gen1):
        if v in d:
           count =d.count(v)
           
        
    
    
    
    
    
    

