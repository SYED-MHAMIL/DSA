


def skipPunctuation(ch):
    return (
            (ord('a')<= ord(ch) <= ord('z')) or (ord('A')<= ord(ch) <= ord('Z')) or (ord('0')<= ord(ch) <= ord('9')) 
        )


def validPalendrom(strs):
    # Was it a car or a cat I saw?
    left =0 
    right = len(strs) -1
    
    while left <= right:
        if not skipPunctuation(strs[left]):
           left+=1
        elif not skipPunctuation(strs[right]):  
            right-=1
        elif  strs[left].lower() != strs[right].lower():
           return False 
        else:
            left+=1
            right-=1
    return True

print(validPalendrom('Was it a?:/// car or a cat I saw?'))
    