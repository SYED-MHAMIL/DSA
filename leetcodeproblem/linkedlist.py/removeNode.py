################################################## 
#                BRUTE FORCE APPROACH
################################################## 




class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
# for head1

head = Node(2)    
head.next = Node(4)    
head.next.next = Node(6)    
head.next.next.next = Node(8)  