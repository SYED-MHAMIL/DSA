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
    temp = None
    while fast and fast.next:
        temp = fast.next
        temp2 = slow.next
        fast.next = slow
        slow.next = temp
        #  1 , 2 , 3 , 4 
        #  2--1----3
        print('slow',slow.data)
        print('Fasr',fast.data)

        print('\n     ===================' )

        slow = temp2.next
        fast = temp.next


    return  header


findnode = swap_nodePair(head)
while findnode:
    print(findnode.data,'-->',end="")
    findnode = findnode.next

print('None')
