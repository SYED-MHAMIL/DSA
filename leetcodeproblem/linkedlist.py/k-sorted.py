from typing import List, Optional


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
# for head1

# first list
list1 = Node(1)    
list1.next = Node(2)    
list1.next.next = Node(4)    
    


# second lisst
list2= Node(1)  
list2.next = Node(3)  
list2.next.next= Node(5)


# third liist


list3= Node(3)  
list3.next = Node(6)



listofLink = list1
listofLink.next = list2 
listofLink.next.next =  list3


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# make the function for k-sorted list
# 1-unedrstand the promblem first
# 2- `brak down the problem `

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
    pass