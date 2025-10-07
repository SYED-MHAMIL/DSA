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

head = Node(2)    
head.next = Node(4)    
head.next.next = Node(6)    
head.next.next.next = Node(8)    
# head.next.next.next.next = Node(5)    
# head.next.next.next.next.next = Node(6)



# *************************************************************************
                #   THROUGH BRUTE FORCE
# *************************************************************************




# def reorderList(header):
#     node = [] # list of nodes
#     curr= header

#     while curr:
#         node.append(curr)
#         curr = curr.next 
#     i,j = 0, len(node) -1
#     while  i<j:
#         node[i].next = node[j] 
#         i+=1
#         if i>=j:
#            break

#         node[j].next = node[i]
#         j-=1  

#     node[i].next = None 
#     return node     
                        
                
# nodes  =reorderList(head)            
# while nodes[0]:
#     print(nodes[0].data)
#     nodes[0]= nodes[0].next 





# *************************************************************************
                #   THROUGH RECURSION
# *************************************************************************


# 1--none

# def reorderList(header):
    
#     def rec(root,curr):

#         if curr:
#             return  root
#         root = rec(root,curr)
#         if not root:
#                 return None

#         tmp = None
#         if root == curr or root.next == curr:
#            curr.next = None 
#         else:
#             tmp = root.next 
#             root.next  =  curr
#             curr.next= tmp
#         #   
#         # 1-2-3-4
#         # 1-3-2-3-4
#         return tmp

#     return rec(header,header.next)


# nodes  =reorderList(head)            
# while nodes[0]:
#     print(nodes[0].data)
#     nodes[0]= nodes[0].next 




def reorderList2( head) :

        def rec(root, cur):
            if not cur:
                return root

            root = rec(root, cur.next)
            if not root:
                return None

            print(f"Linking root={root.data} and cur={cur.data}")

            tmp = None
            if root == cur or root.next == cur:
                print(f"Stop condition reached at {cur.data}")
                cur.next = None
            else:
                tmp = root.next
                root.next = cur
                cur.next = tmp
                print(f"Connected {root.data} -> {cur.data} -> {tmp.data}")
                 
            return tmp

        rec(head, head.next)
        return head


e = reorderList2(head)
# print(e.data)
while e is not None:
    print(e.data)
    e= e.next