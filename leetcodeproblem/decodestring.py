
deocoded="3[a2[bc]5[t]]"
alphabet = 'abcdefghijklmnopqrstwuvxyz'
numberStack = []
stringStack = []
for i in deocoded:

    if i == ']':
       
       popOutch =[]
       while True:
            ch = stringStack.pop()
            if ch == '[':
                break
            # stringCheck = ch
            # if ch.lower() in alphabet:
            popOutch.append(ch) 
                                    
       popOutnumber =  numberStack.pop()
       popOutnumberInt = int(popOutnumber)  
       stringStack.append(''.join(popOutch)* popOutnumberInt)

    
    if i.isdigit():
       numberStack.append(i)
    elif i != "]":
        stringStack.append(i)
# res = []

print(stringStack)
# print(numberStack)
   








#         #   while True:
#         #     lbrace = stringStack.pop()
#         #     if lbrace == '[':
#         #         break
#         #     popOutch =''
#         #     stringCheck = stringStack.pop()
#         #     if stringCheck.lower() in alphabet:
#         #        popOutch+= stringStack.pop() 

#         #     popOutnumber =  numberStack.pop()
#         #     popOutnumberInt = int(popOutnumber)  
#         #     stringStack.append(popOutch * popOutnumberInt)



