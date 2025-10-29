# Merge Two Sorted Linked Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]




# ********************************************************************************
                    #        Iteration with pointer
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
# head.next.next = Node(4)    
# head.next.next.next = Node(6)    

# for  head 2

head2 = Node(1)    
head2.next = Node(3)    
# head2.next.next = Node(5)    
# head2.next.next.next = Node(7)    

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








# reversehead = mergedWithIteration2(head,head2)
# printList(reversehead)



def mergedWithIteration3(head1,head2):
     head = head1
     preserveHead1Next = head1.next 
     
     # Input: list1 = [1,2,4,6], list2 = [1,3,5,7]
     # Output: [1,1,2,3,4,5] 
     while preserveHead1Next and head2:
           head1.next = head2 
           head2Preserve = head2.next
           head2.next = preserveHead1Next
        #    1--1--2
           head1 = preserveHead1Next
           preserveHead1Next = preserveHead1Next.next   
           head2 = head2Preserve 
           head1.next = head2
           

     return head            

     

# reversehead = mergedWithIteration3(head,head2)
# printList(reversehead)





# *************************************************************
    #            ITERATION BUT READABLE
# *************************************************************


#  Iteration
# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def mergedWithIteration4(head1,head2):
    dummy = node  =  ListNode()
#   for example:  list1= [1,2,4] , list2 =[1,3,5]
    while head1 and head2:
        if head1.data < head2.data:
            node.next = head1
            head1= head1.next 
        else:
            node.next = head2
            head2= head2.next 
        node = node.next   
    node.next = head1 or head2 
    return dummy.next

    
           

     

# mergedHead= mergedWithIteration4(head,head2)
# printList(mergedHead)






#*******************************************************************************
                    #      RECURSION   METHOD
#*******************************************************************************

print("""
             ***********    with the help of Pointer method    ***********
""")



def mergedWithRecursion(head1,head2):
    # Input: list1 = [1,2], list2 = [1,3]
    # Output: [1,1,2,3]

    if head1 is None:
        return head2
    if head2 is None:
        return head1
        

    if head1.data <= head2.data:
       head1.next = mergedWithRecursion(head1.next,head2)
       return head1 
    else:
        head2.next = mergedWithRecursion(head1,head2.next)
        return head2       
    
    

    

# 1,1,2,3,4,5
# 5
mergedHead = mergedWithRecursion(head,head2)
printList(mergedHead)




# under the hoodo it works like this
# def fac(3):
#      return 3* fac(2):
#             return 2 *fac(1):
#                   reutrn 1 * 1                    


# def get_table(n,i=1):
#     if i == 11:
#        return []
#     return ([n*i] if (n*i % 2) != 0 else []) + get_table(n,i+1)

# print(get_table(5))


