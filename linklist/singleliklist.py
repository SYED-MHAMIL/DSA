# #****************************************************************************
# #                               Linked List Data Structure
# #****************************************************************************


# # A linked list is a fundamental data structure in computer science. It mainly allows efficient insertion and deletion operations compared to arrays. Like arrays, it is also used to implement other data structures like stack, queue and deque. Here’s the comparison of Linked List vs Arrays

# # Data Structure: Non-contiguous
# # Memory Allocation: Typically allocated one by one to individual elements
# # Insertion/Deletion: Efficient
# # Access: Sequential
# # Array:

# # Data Structure: Contiguous
# # Memory Allocation: Typically allocated to the whole array
# # Insertion/Deletion: Inefficient
# # Access: Random



# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None
# node0 = Node(80)    
# node1 = Node(10)    
# node2 = Node(20)    
# node3 = Node(30)    
# node4 = Node(40)    

# node1.next =  node2 
# node2.next =  node3 
# node3.next =  node4  
# head = node1
# new_head = node0   #  insert at first
# new_head.next = head 
# head  =  new_head
# current = head
# while current.next is not None:
#       print(current.data)
#       current = current.next  
# # print("None")

# node5 = Node(50)
# current.next = node5   # at the end   
# # print()
# print(current.data)


   
# # *****************************************************************************
    #                           DELTE AT THE FIRST NODE
# # *****************************************************************************
# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None
    
# node1 = Node(10)    
# node2 = Node(20)    
# node3 = Node(30)    
# node4 = Node(40)    

# node1.next =  node2 
# node2.next =  node3 
# node3.next =  node4  
# head = node1

# if head.next is not None:
#     head = head.next  

    
# current = head
# while current is not None:
#       print(current.data)
#       current = current.next  












# # *****************************************************************************
    #                           DELETE AT THE END NODE
# # *****************************************************************************
# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None
    
# node1 = Node(10)    
# node2 = Node(20)    
# node3 = Node(30)    
# node4 = Node(40)    

# node1.next =  node2 
# node2.next =  node3 
# node3.next =  node4  
# head = node1

# current = head
# while current.next.next is not None:
#       print(current.data)
#       current = current.next  
# current.next =   None
# print(current.next) 







# # *****************************************************************************
    #                           INSERTION BETWEEN  NODE
# # *****************************************************************************
# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None
    
# node1 = Node(10)    
# node2 = Node(20)    
# node3 = Node(30)    
# node4 = Node(40)    
# addNodeinMid = Node(25)    

# node1.next =  node2 
# node2.next =  node3 
# node3.next =  node4  
# head = node1

# current = head
# while current is not None and  current.data != 20:
#       print(current.data)
#       current = current.next  
# addNodeinMid.next =  current.next
# current.next = addNodeinMid   


# while current is not None :
#       print(current.data)
#       current = current.next  












# # *****************************************************************************
#                               DELETING BETWEEN  NODE
# # *****************************************************************************
# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None
    
# node1 = Node(10)    
# node2 = Node(20)    
# node3 = Node(30)    
# node4 = Node(40)    
# addNodeinMid = Node(25)    

# node1.next =  node2 
# node2.next =  node3 
# node3.next =  node4  
# head = node1

# current = head
# while current.next is not None and  current.next.data != 20:
#       print(current.data)
#       current = current.next  
# current.next = current.next.next 
# # print(current.data, end=".")

# while current is not None :
#       print(current.data)
#       current = current.next  













# # *****************************************************************************
#                               UPDATing BETWEEN  NODE
# # *****************************************************************************
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
node1 = Node(10)    
node2 = Node(20)    
node3 = Node(30)    
node4 = Node(40)    
addNodeinMid = Node(25)    

node1.next =  node2 
node2.next =  node3 
node3.next =  node4  
head = node1

current = head
while current is not None and  current.data != 20:
      print(current.data)
      current = current.next  
addNodeinMid.next =  current.next
current.next = addNodeinMid   


while current is not None :
      print(current.data)
      current = current.next  









