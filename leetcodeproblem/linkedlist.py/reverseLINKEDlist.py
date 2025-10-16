# Description
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# Example 2:

# Input: head = []

# Output: []
# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000

def reverse(head):
    if head.next == None:
       return head
    rest= reverse(head.next)

    head.next.next= head
    
    print(head.next.data,'--->',head.data)
    head.next = None
    
    
    return rest 
    

# print(reverse())







# **************************************************************************************************
#                           Using recurtion(stack)
# **************************************************************************************************


# def reverseNode(head):
#     if head is None or head.next is  None:
#        return head    
#     res = reverseNode(head.next) 
    
    
#     head.next.next = head 
#     head.next  = None



# #----------------------- EXPLANATION------------------------

#     # first step lets suppose when head is 4
#   #   1-->2-->3-->4-->-->5-->None  =
#   #  1-->2-->3-->5-->4
    
    
#     # second step lets suppose when head is 3
#   #   1-->2-->3-->4-->-->5-->None  =
#   #   1-->2-->5-->4-->3

   
#     # third step lets suppose when head is 2
#   #   1-->2-->3-->4-->-->5-->None  =
#   #   1-->5-->4-->3-->2


#        # third step lets suppose when head is 2
#   #   1-->2-->3-->4-->-->5-->None  =
#   #   5-->4-->3-->2-->1--None

    
#     head.next = None
#     return res


def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()



class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
head = Node(1)    
head.next = Node(2)    
head.next.next = Node(3)    
head.next.next.next= Node(4)


reversehead = reverse(head)
printList(reversehead)













class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None
def reverseList(head):
      if head is None or head.next is None :
          return head
 
      # reverse the rest of linked list and put the
      # first element at the end
      rest = reverseList(head.next)

      # make the current head as last node of
      # remaining linked list
      head.next.next = head
      
      
      #update next of current head to NULL
     #break the connection for forward link 
      head.next = None

      return rest


def printList(node):
    # 1 -> 2 -> 3 -> 4 -> 5
    while node is not None:
         print(node.data,end="")
         if node.next is not None:
            print(end="-->")
         node = node.next
    print(  )
if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverseList(head)
    # printList(head)










# **************************************************************************************************
#                           Using ittationk ( threee pointer)
# **************************************************************************************************
def reverseNodebyIteration( head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
#       none 1--2--3
        # 3-2-1-None
        # first step when curr is  1 :
        #  1--None
        
        # Second step when curr is  2 :
        #  2--1--None

        # third step when curr is  3 :
        #  3--2--1--None
 

   
        return prev
def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()



class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
head = Node(1)    
head.next = Node(2)    
head.next.next = Node(3)    
head.next.next.next= Node(4)


reversehead = reverseNodebyIteration(head)
# printList(reversehead)




