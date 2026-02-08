 # Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: [0, 0, 1, 1, 2, 2] has all 0s first, then all 1s and all 2s in last.

# Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
# Explanation: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.


def dudge_national(arr):
    l = 0 
    m = 0 
    h = len(arr) - 1
    
    while m <= h:
        val = arr[m]
        if val  == 0:
           arr[l],arr[m] = arr[m],arr[l]
           m+=1
           l+=1
        elif val == 1:
           m+=1
           print(m,h)
        else:
           arr[h],arr[m]  = arr[m],arr[h]
           h-=1    
    return arr 

dnf= dudge_national([2,0,1]) 
print(dnf)