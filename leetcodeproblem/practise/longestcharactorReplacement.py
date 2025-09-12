
def longestrepeatedCharactor(string,k):
    res= 0
    #  string = AAABABB ,k =1
    for i in range(len(string)):
        hash_Table= {}
        max_val =0 
        for j in range(i,len(string)):
            # AAAB
            hash_Table[string[j]] = hash_Table.get(string[j], 0) +1 
             
            max_val =  max(hash_Table[string[j]],max_val)
            lengthofSubs = len(string[i:j+1])            
            kth_elemnet = lengthofSubs -  max_val
            if k>=kth_elemnet:                
               res = max(lengthofSubs,res) 
        print("inner off")
    return res 

print(longestrepeatedCharactor('AAAB',k=1))            