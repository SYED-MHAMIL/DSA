# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                   KTh most frequent element
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Input: nums = [1,2,2,3,3,3], k = 2
def kthMostfrequentUsingsort(arr,k):
    freq= {}
    for i in arr:
        freq[i] = freq.get(i,0) +1

    if len(arr) <=k:
       print("somthing is wrong basically  you are giving most frequency from data")
       return arr 
    
    # sortedItem = sorted(freq,key= )
    sortedItem = sorted(freq.items(),key= lambda x:(-x[1],x[0]))
    # return sortedItem
    getKth = [i for i in arr if i>=sortedItem[k-1][0]]    
    sortedKth = sorted(getKth,reverse=True)
    return sortedKth
print(kthMostfrequentUsingsort([1,2,2,3,3,3],2))


def findKthmostFrequent(numsArray,k):
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


# print(findKthmostFrequent([1,2,2,3,3,3],2))

     