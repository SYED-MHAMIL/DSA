palendrom ="madam"


# def is_palendrom(text):
#     text = str(text)
#     if text[0] != text[-1]:
#         return False
#     if len(text) <=1:
#         return True 
#     return is_palendrom

# if is_palendrom(palendrom):
#    print("wow that's are palaendrom")
# else:
#     print("sorry,that's are not palaendrom ")





# annother eay to solve


def is_palendrom(text):
    text = str(text)
    if text != text[::-1]:
        return False
    else:
        return True 
    
print(
is_palendrom("wow"))
