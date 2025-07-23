# def timeConversion(s):
#     # Write your code here
#     if "PM" in s:
#         r=s.replace("PM","")
#         r =r.split(':')
#         f=str(int(r[0])+12)
#         f2 =":".join(r[1:])
#         return f+":"+f2
       
        
#     else:
#         return (s.replace("AM",""))
# print(timeConversion("12:05:45PM"))




# 100% correct format

def timeConversion(time_Str):

    
    period = time_Str[-2:]
    hh ,mm , ss =map(int,time_Str[:-2].split(":"))
    if period == "AM":
        if hh == 12:
            hh=0
    else:
        if hh != 12:
            hh+=12
            
        
    return f"{hh}:{mm}:{ss}"
print(timeConversion("11:05:45PM"))
    
    
    