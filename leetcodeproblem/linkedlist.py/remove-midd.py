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
# head.next.next = Node(3)    
# head.next.next.next = Node(4)  
# head.next.next.next.next = Node(5)  

def removeMid(header):
    if not header.next or header:
        return None
    
    left = header
    right = header 
    prev= None
    # 1 , 2 
    # prev = 1
    # left = 2
    #  right  = 3
    while right and right.next:
        prev = left
        left= left.next
        right = right.next.next  

    prev.next = left.next
    return  header   


he = removeMid(head)
while he:
    print(he.data,'-->',end="")
    he = he.next 
print('None')









