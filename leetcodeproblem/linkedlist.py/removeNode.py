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
#     index =  len(arr) -n  

#     arr.pop(index)
#     if not arr:
#        return None   
    
#     before = index -1
#     after =  index 
#     arr[before].next =  arr[after]   
      
#     while arr[0]:
#         print(arr[0].data)
#         arr[0] =arr[0].next 

# main()








################################################## 
#                Two pointer
##################################################



def main():
    first =  head 
    second = head
    newsEc= second 
    n =2
    step =1 
    
    while step < n :
        first = first.next 
        step+=1
    
    while  first and first.next :
        first = first.next 
        second = second.next 

    second.next = first
    return newsEc 


h = main()
while h:
    print(h.data)
    h = h.next
    