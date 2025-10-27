# 🧩 5. Swap Nodes in Pairs

# Concept: Traversal and relinking nodes in pairs.

# Example:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]





class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
# for head1

head = Node(1)    
head.next = Node(2)    
head.next.next = Node(3)    
head.next.next.next = Node(4)  
# head.next.next.next.next = Node(5)  


def swap_nodePair(header):
    # if not   header and not header.next:
    #     return None
    slow = header
    fast = header.next
    prev = None
    res = fast
    isApply = False


    while slow and fast:
        # 1 ---- 2 --- 3
         temp = fast.next
         fast.next = slow
         slow.next  =temp
        #  2--1---3---4
         if isApply:
            print("aapply")
            prev.next = fast
         
         isApply = True
         prev = slow
        #  prev = 1
         if temp:
            slow =  temp
            fast = temp.next
         else:
             break

    return  res


findnode = swap_nodePair(head)
while findnode:
    print(findnode.data,'-->',end="")
    findnode = findnode.next

# print('None')
