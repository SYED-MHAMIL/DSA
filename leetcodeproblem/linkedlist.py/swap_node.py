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
    slow = header
    fast = header.next
    prev = None
    res = fast
    while fast and fast.next:
        temp = fast 
        temp2 = slow.next 
        
        prev.next = fast
        fast.next = slow
        #  2-1
        slow.next = temp.next


        prev =slow
        fast = temp.next.next
        slow = temp2.next 
    
    
    
    return  res


findnode = swap_nodePair(head)
while findnode:


    print(findnode.data,'-->',end="")
    findnode = findnode.next

# print('None')
