# ***********************************************************
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

        
        



        