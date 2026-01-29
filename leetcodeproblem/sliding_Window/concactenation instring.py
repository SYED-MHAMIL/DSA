def findSubstring( s, words) :
        s_ele = [0]*26
        words_ele = [0]*26
        
        word =''
        for w in words:
            word+=w
        
        
        for i in range(len(word)):
            words_ele[ord(word[i]) -ord("a")]+=1
            s_ele[ord(s[i]) -ord("a")]+=1
        
        
        match = 0
        for i in range(26):
            match+= 1 if words_ele[i] == s_ele[i] else 0 

        l =0 
        result=  []
        for r in range(len(word),len(s)):
            if  len(word) >  len(s):
                return []
            
            if match == 26: 
               result.append(l)
               print({"words": words_ele ,"s_le":s_ele})
                   
            print("iindecc",r)
            index = ord(s[r]) - ord("a")
            s_ele[index]+=1

            if s_ele[index] == words_ele[index]:
                match+=1
            elif s_ele[index] == words_ele[index]+1:
                 match-=1
            
            
            index = ord(s[l]) - ord("a")
            s_ele[index]-=1

            if s_ele[index] == words_ele[index]:
                match+=1
            elif s_ele[index] == words_ele[index]-1:
                 match-=1
            l+=1

        if match == 26:
           result.append(l)
        return result    
    

print(findSubstring(s = "wordgoodgoodgoodbestword", words =["word","good","best","word"]

))