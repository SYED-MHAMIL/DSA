# Description
# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

# Note: index is not given to you as a parameter.




#***********************************************************
            #    BRUTE FORCE  
# *******************************************************************



class Solution:
    def hasCycle(self, head) -> bool:
        hash_map = set()
        while head is not None:
            if head.next in hash_map:
                return True
            hash_map.add(head.next)        
            head = head.next    
        return False
    




# ***********************************************************
            #    Two Pointer
# *******************************************************************
 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
         
        slow = head
        fast=  head
        while fast and fast.next:
            slow = slow.next
            fast=  fast.next.next    
            if fast == slow:
                return True
        return False

        
        



        