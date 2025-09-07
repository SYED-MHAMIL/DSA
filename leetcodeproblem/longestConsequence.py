def consequetiveSequence(arr):
    # Input: nums = [2,20,4,10,3,4,5]
    arr2=arr
    arr2.sort()
    con_arr = [arr2[0]]
    prev =arr2[0]
    for ch in range(1,len(arr2)):
        conSequence = prev +1
        if conSequence == arr2[ch]:
           con_arr.append(arr2[ch]) 
        prev =arr2[ch]

    return len(con_arr)

# print(consequetiveSequence([40,1,2,8,5,34,3,4]))

        

#  optimize way to solve this 


def conseSequenceOptimize(arr):
    setter = set(arr)
    print(setter)
    seq_start = 0
    res = []
    for i in setter:
        exits = i-1
        if not exits in setter:
            seq_start = i
            print('start ele',seq_start) 
            break
    res.append(seq_start)
    previos = seq_start

    for i in range(len(arr)):
        previos+=1

        if previos in setter:
            res.append(previos)
    return len(res)

print(conseSequenceOptimize([22,40,2,20,4,5,3]))