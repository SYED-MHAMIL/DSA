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










# def reverseLinkedList(head) :
#     sort = reverseLinkedList(head.next)
    

    


def rec(n):
    if n == 0:
        return 1
    
    res = n* rec(n-1)
    print(n)
    return res  
print(rec(5))