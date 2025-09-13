# ******************************************************************************
        #                  Brute  force method  
# ******************************************************************************



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

# print(longestrepeatedCharactor('AAAB',k=1)) 




# ******************************************************************************
        #                  TWO POINTER METHOD  
# ******************************************************************************



def lonCharactorReplacement(s,k):
    res = 0 
    charSet = set(s)
    for c in charSet:
        count = l = 0
        for right in range(len(s)):
            if s[right] == c:
                count+=1
            while (right - l +1) - count > k:
                if s[l] == c:
                    count-=1
                l+=1
            res = max(res,right - l +1)
    return res
print(lonCharactorReplacement("ABAABB" ,1))    
    


















# ******************************************************************************
        #                  TWO POINTER METHOD OPTIMAL  
# ******************************************************************************

def longestrepeatedCharactorPinter(s,k):
    res= 0
    hash_Table= {}
    l= 0
    max_f = 0  
    #  string = AAABABB ,k =1
    for r in range(len(s )):
        hash_Table[s[r]] = hash_Table.get(s[r],0) +1
        max_f = max(max_f,hash_Table[s[r]])

        

        while (r-l+1) - max_f > k :
            hash_Table[l]-=1 
            l+=1         

        res = max(r-l+1,res)
    
    return res 


print(longestrepeatedCharactorPinter('AAAB',k=1)) 

def pointerRepeatCharactor(s,k):
    # substring frequencies
    hash = {} 
    
    max_f = 0 
    l = 0  
    res= 0 
    for right in range(len(s)):
        # put the substring with thier ferequencies
        hash[s[right]] = hash.get(s[right],0) +1
        # get the max frequencies 
        max_f = max(max_f,hash[s[right]])
        
        # if got the value which i not aplicable
        while (right-l+1) - max_f > k:
            #  reduce the sliding window 
             l+=1
            #  remove that element which has been reduced
             hash[s[l]]-=1
        res = max(res,right-l+1)    
    return res 
print(pointerRepeatCharactor('AABDAA',1))        




