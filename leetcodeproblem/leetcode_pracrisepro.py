# Input: nums = [1,2,2,3,3,3], k = 2

def findAnagram(numsArray,k):
    bukcets = [[] for _ in range(len(numsArray))]
    freq = {}
    kth_el = []
    for num in numsArray:
        freq[num]= freq.get(num,0) +1
    for num in numsArray:
        bukcets[freq[num]].append(num)
    
    for index in range(len(bukcets)-1,-1, -1):
        for nums in bukcets[index]:
          if bukcets[k][0] <= nums: 
             kth_el.append(nums)

    return kth_el    


print(findAnagram([1,2,2,3,3,3],2))

     
