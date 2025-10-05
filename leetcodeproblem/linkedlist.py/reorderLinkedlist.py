# Reorder Linked List
# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:

# [0, 1, 2, 3, 4, 5, 6]

# Reorder the nodes of the linked list to be in the following order:

# [0, 6, 1, 5, 2, 4, 3]

# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

# [0, n-1, 1, n-2, 2, n-3, ...]

# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

# Example 1:

# Input: head = [2,4,6,8]

# Output: [2,8,4,6]
# Example 2:

# Input: head = [2,4,6,8,10]

# Output: [2,10,4,8,6]
# Constraints:

# 1 <= Length of the list <= 1000.
# 1 <= Node.val <= 1000







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
head.next.next.next.next.next = Node(6)  




def reorderList( head):
        left = head
        right = [] 
        curr = head
        res = head
        result  = res

        # Input: head = [2,4,6,8]
        # Output: [2,8,4,6]

        while curr:
            right.append(curr)
            curr= curr.next
        index=len(right) - 1  
        
        
        while left.data < right[index].data:
              res.next = right[index]
              prev = right[index]
              left  = left.next
              if left.data >= right[index].data:
                  break 
              prev.next = left
              res = left
              if index >= 0:
                 index-=1 
                 
                 
        # res.next = None
        return result



                
node  =reorderList(head)            
while node:
     print(node.data)
     node = node.next

print(node)














def reorderList(header):
    node = [] # list of nodes
    curr= header

    while curr:
        node.append(curr)
        curr = curr.next 
    i,j = 0, len(node) -1
    while  i<j:
        node[i].next = node[j] 
        i+=1
        if i>=j:
           break

        node[j].next = node[i]
        j-=1  

    node[i].next = None 
    return node     
                        
                
nodes  =reorderList(head)            
# while nodes[0]:
#     print(nodes[0].data)
#     nodes[0]= nodes[0].next 


