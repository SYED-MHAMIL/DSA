class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_backspace = 0
        t_backspace = 0 
        s_index = len(s) -1
        t_index  = len(t) -1

        while True :
            # Input: s = "ab#c", t = "ad#c"
            # Input: s = "ab##", t = "c#d#"
            # Input: s = "a#c", t = "b"
    
            while s_index >= 0 and (s_backspace or s[s_index] == "#") :
                  s_backspace+=1 if s[s_index] == "#" else -1
                  s_index-=1
            
            while t_index >= 0 and (t_backspace or t[t_index] == "#") :
                  t_backspace+=1 if t[t_index] == "#" else -1
                  t_index-=1
            
            if not (s_index >=0 and t_index >=0  and s[s_index] == t[t_index]):
               print(s_index)
               print(t_index)
               
               return s_index == t_index == -1
            
            t_index-=1
            s_index-=1
                

s= Solution().backspaceCompare("ab##","c#d#")
print(s)



