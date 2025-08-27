# **************************************************************************
#                     Brute  Force  Method 
# **************************************************************************
import re

def isPalendrom(strs):
    string=''
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', strs).lower()
    for i in range(len(cleaned_text) -1,-1,-1):
        # if isinstance(cleaned_text[i],int) or isinstance(strs[i],str):
           string+=cleaned_text[i]
    if cleaned_text == string:
        return True 
    return False
# print(isPalendrom('Was it a car or a cat I saw?'))




# *************************************************************************
#                    Two  Pointer  Method
# *************************************************************************


import re

def isPalendrom2(strs):
    
    left =0 
    right=len(strs) -1
    while left <= right:
        if not strs[left].isalnum() :
           left+=1
        elif  not strs[right].isalnum() :
           right-=1  
        else :
            if strs[left].lower() != strs[right].lower():
               return False
            left+=1
            right-=1
    return True    
            
print(isPalendrom2('Was it a car or a cat I saw?'))