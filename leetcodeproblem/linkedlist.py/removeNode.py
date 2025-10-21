 ################################################## 
 #                BRUTE FORCE APPROACH
 ################################################## 




# You are given the beginning of a linked list head, and an integer n.

# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:

# Input: head = [1,2,3,4], n = 2
# 4-2 
# 1-1 =>0
# Output: [1,2,4]


class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    
# for head1

head = Node(1)    
head.next = Node(2)    
head.next.next = Node(3)    
head.next.next.next = Node(4)  
head.next.next.next.next = Node(5)  


# def main():
#     arr = []
#     temp = head
#     while temp:
#         arr.append(temp)
#         temp = temp.next 
    
#     n = 2
#     removeIndex =  len(arr) -n
#     if removeIndex == 0: 
#         return head.next

#     arr[removeIndex -1] = arr[removeIndex].next
    
#     return arr
    
 
# headremove = main()
# while headremove:
#     print(headremove.data)
#     headremove = headremove.next  





 ################################################## 
 #                Iteration APPROACH
 ################################################## 




# def main(n=4):
#     N = 0 
#     curr = head 

#     while curr :
#         N+=1
#         curr = curr.next 
    
#     removeIndex =  N - n
#     if removeIndex == 0 :
#         return head.next
#     temp = head

#     for i in range(N-1):
#         if (i+1) == removeIndex:
#           temp.next =  temp.next.next 
#           break
          
#         temp = temp.next       

#     return head
    




    
# headremove = main()
# while headremove:
#     print(headremove.data)
#     headremove = headremove.next  






################################################## 
#                Two pointer
##################################################

# 

# def main(n =3):
#   dummy = Node(0)
#   dummy.next = head

#   first = dummy  
#   second = dummy 
  
#   step = 0 
#   while step != n:
#        first = first.next 
#        step+=1
#   while  first and first.next:
#        first=first.next
#        second=second.next     
#   tri = second.next.next
#   second.next =  tri
#   return dummy.next




# h = main()
# while h:
#     print(h.data)
#     h = h.next
    



# print("aLL RIGHT ")









 ################################################## 
 #                RECURCISE APPROACH
 ################################################## 



def main(head,n):
    
    
    if not head:
       return None
    
    head.next = main(head.next,n) 
    n[0]-= 1
    if n[0] == 0:
        return head.next
    return head
    
headremove = main(head,n=[2])
while headremove:
    print(headremove.data , "-->",end="")
    headremove = headremove.next  
print("none")
