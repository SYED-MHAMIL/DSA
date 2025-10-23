class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
# for head1

head = Node(1)    
# head.next = Node(2)    
# head.next.next = Node(3)    
# head.next.next.next = Node(4)  
# head.next.next.next.next = Node(5)  


def find_end(header,n):
    dummy = Node(0)
    dummy.next = header
    slow = dummy
    fast = dummy 
    
    step = 0 
    while step != n:
        fast= fast.next 
        step+=1

    while fast and fast.next:
        fast=  fast.next
        slow = slow.next


    return  slow.next

findnode = find_end(head,1)
print(findnode.data,)
    
    


    