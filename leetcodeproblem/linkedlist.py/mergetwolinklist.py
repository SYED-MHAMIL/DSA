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



# Input: list1 = [1,2,4,6], list2 = [1,3,5,7]
# Output: [1,1,2,3,4,5]

def mergedWithIteration(head1,head2):
    head = head1
    preverseHead1= head1.next 
    
    while preverseHead1 and head2:
          head1.next = head2   #link
          temp =  head2.next  # store
          head2.next = preverseHead1   
        #   1--1---2 
          head1 = preverseHead1
          
          preverseHead1 = preverseHead1.next
          head2 = temp
          head1.next = head2
        #   1--1---2--3--4--5 

    return head              
          
           

    






def printList(head):
    while head is not None:
        print(head.data ,end="-->")
        head = head.next
        # if head.next is not  None :
        #     print(end="-->")
    print("None")        





class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    

# for head1

head = Node(1)    
head.next = Node(2)    
head.next.next = Node(4)    
head.next.next.next = Node(6)    

# for  head 2

head2 = Node(1)    
head2.next = Node(3)    
head2.next.next = Node(5)    
head2.next.next.next = Node(7)    

# reversehead = mergedWithIteration(head,head2)
# printList(reversehead)







def mergedWithIteration2(head1,head2):
    head = head1 
    preserveHead1 = head1.next
    
# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5] 
    while preserveHead1 and head2:
        head1.next= head2  #link
        # 1--1--3--5 
        # first preserve the list 3,5
        saveHead2List = head2.next
        head2.next = preserveHead1
        # 1--1--2
        head1 = preserveHead1
        preserveHead1= preserveHead1.next 
        head2 =  saveHead2List


        head1.next = head2
        # 1--1--2--3

        # 

        return head


reversehead = mergedWithIteration2(head,head2)
printList(reversehead)





#*******************************************************************************
                    # POINTER Method
#*******************************************************************************
