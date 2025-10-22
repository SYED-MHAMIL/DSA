# Problem

# Given the head of a linked list, delete the middle node and return the modified list.

# Constraints

# 1
# ≤
# number of nodes
# ≤
# 10
# 5
# 1≤number of nodes≤10
# 5

# Edge Cases

# Only one node → return None

# Even number of nodes → remove the second middle node (as per LeetCode standard)

# Approach

# Use slow and fast pointers to find the middle, track the previous node, and remove it.



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

def removeMid(header):
    left = header
    rihgt = header.next 
    prev= header
    
    if not header.next:
        return None
    
    







