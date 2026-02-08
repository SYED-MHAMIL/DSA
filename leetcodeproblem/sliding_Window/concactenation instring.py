# def findSubstring( s, words) :
#         s_ele = [0]*26
#         words_ele = [0]*26
        
#         word =''
#         for w in words:
#             word+=w
        
        
#         for i in range(len(word)):
#             words_ele[ord(word[i]) -ord("a")]+=1
#             s_ele[ord(s[i]) -ord("a")]+=1
        
        
#         match = 0
#         for i in range(26):
#             match+= 1 if words_ele[i] == s_ele[i] else 0 

#         l =0 
#         result=  []
#         for r in range(len(word),len(s)):
#             if  len(word) >  len(s):
#                 return []
            
#             if match == 26: 
#                result.append(l)
#                print({"words": words_ele ,"s_le":s_ele})
                   
#             print("iindecc",r)
#             index = ord(s[r]) - ord("a")
#             s_ele[index]+=1

#             if s_ele[index] == words_ele[index]:
#                 match+=1
#             elif s_ele[index] == words_ele[index]+1:
#                  match-=1
            
            
#             index = ord(s[l]) - ord("a")
#             s_ele[index]-=1

#             if s_ele[index] == words_ele[index]:
#                 match+=1
#             elif s_ele[index] == words_ele[index]-1:
#                  match-=1
#             l+=1

#         if match == 26:
#            result.append(l)
#         return result    
    

# print(findSubstring(s = "wordgoodgoodgoodbestword", words =["word","good","best","word"]

# ))



# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#       required_words ={}
#       current_words = {}
#       required_wordsLength = len(set(words))
#       each_words = len(words[0])
#       print("each_words",each_words)
      
      
#       chractor_len =  0 
#       for i in words:
#         chractor_len+=len(i)
#         required_words[i] = required_words.get(i,0)+1
      
#       for i in range(0,chractor_len,each_words):
#           current_words[s[i:i+each_words]] = current_words.get(s[i:i+each_words],0)+1

#       match = 0 
#       for word in set(words):
#           match+=1 if required_words[word] == current_words.get(word,0) else 0


#       result=[]
#       l= 0 
#       print(current_words)
#       for r  in range(chractor_len,len(s),each_words):
#          if match == required_wordsLength:
#              result.append(l)
     
#          current_words[s[l:l+each_words]]-=1
           
         
#          if required_words.get(s[l:l+each_words],0) == current_words.get(s[l:l+each_words],0):
#             match+=1
#          elif required_words.get(s[l:l+each_words],0)-1 == current_words.get(s[l:l+each_words],0):
#             match-=1
#          l+=each_words

#          #move right
#          current_words[s[r:r+each_words]]= current_words.get(s[r:r+each_words],0)+1
#          if required_words.get(s[r:r+each_words],0) == current_words.get(s[r:r+each_words],0):
#             match+=1
#          elif required_words.get(s[r:r+each_words],0)+1 == current_words.get(s[r:r+each_words],0):
#             match-=1
    
#       if match ==  required_wordsLength :
#            result.append(l)
    
#       return result
    
# obj =  Solution()
# print(obj.findSubstring("[lingmindraboofooowin]gdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))





class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        result = [] 
        offset=  len(words[0])
        k = len(set(words))
        required_words = {}
        for w in words:
            required_words[w] = required_words.get(w,0)+1
        k = len(words)
        
        for start in range(0,offset):
            count =0
            seen = {}
            left= start

            for right in range(start,len(s),offset):
                word =  s[right:right+offset]
                
                if word in required_words:
                   seen[word] = seen.get(word,0) + 1
                   count+=1
            
                   
                   while seen[word] > required_words[word]:
                         leftWord = s[left:left+offset]
                         count-=1
                         seen[leftWord]-=1
                         left+= offset 

                   if  k == count :
                       result.append(left)                   

                else:
                    count = 0 
                    seen.clear()
                    left=right+offset
        return  result   


find = Solution()
print(find.findSubstring( s = "barfoothefoobarman", words = ["foo","bar"])) 