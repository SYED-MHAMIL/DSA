# Merge Two Sorted Linked Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]




# ********************************************************************************
                    #        Iteration 
# ********************************************************************************



# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]

def mergedWithIteration(head1,head2):
    head = head1

    preservedhead1 = head1.next
    while head1 and head2:
        head1.next = head2 
        
        head1.next.next = preservedhead1
        # 1--1--3--4
        if preservedhead1: 
           preservedhead1 = preservedhead1.next
        head1=head1.next #3
        head2= head2.next # 5  
    
    return head







def printList(head):
    while head is not None:
        print(head.data ,end="")
        head = head.next
        # if head.next is not  None :
        #     print(end="-->")
            

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    

# for head1

head = Node(1)    
head.next = Node(2)    
head.next.next = Node(4)    

# for  head 2

head2 = Node(1)    
head2.next = Node(3)    
head2.next.next = Node(5)    

reversehead = mergedWithIteration(head,head2)
printList(reversehead)



