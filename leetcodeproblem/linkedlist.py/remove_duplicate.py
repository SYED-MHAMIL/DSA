# 🧩 2. Remove Duplicates from Sorted Linked List

# Concept: Traverse and skip duplicate nodes in place.

# Example:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]



class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
# for head1

head = Node(1)    
head.next = Node(2)    
head.next.next = Node(3)    
head.next.next.next = Node(4)  
head.next.next.next.next = Node(5)  
