from typing import List, Optional


class Node:
    def __init__(self,val):
        self.val = val 
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

#  
listofLink = [list1,list2,list3]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# make the function for k-sorted list

# 1-unedrstand the promblem first
# 2-  `brak down the problem `
# 3- Write in paper 
# 4-  write in code 
# 5- Now use the optize solution



#==========================================================================================================================
#                            Brute fofrce approaach
#==========================================================================================================================

# def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
#     nodes= []

#     for lst in lists:
#         while lst:
#             nodes.append(lst.data)
#             lst = lst.next 
#     nodes.sort()
#     dummy = ListNode(0)
#     curr = dummy
#     for node in nodes:
#         curr.next = ListNode(node)
#         curr = curr.next
        
    
#     return dummy.next

        
# listofmerge =mergeKLists(listofLink)
# while  listofmerge:
#     print(listofmerge.val)
#     listofmerge= listofmerge.next

        







#==========================================================================================================================
#                            Iteration approaach
#==========================================================================================================================










# def mergeKListsiteration( lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         res = ListNode(0)
#         cur = res

#         while True:
#             minNode =  -1 
#             for i in range(len(lists)):
#                 if not lists[i]:
#                    continue
#   #     Input: lists = [[null] , [null] , [6]]
#                 if minNode == -1 or lists[i].val < lists[minNode].val :
#                     # pass
#                     minNode = i 
#             if minNode == -1:
#                break        
                       
#             cur.next = lists[minNode]
#             lists[minNode] = lists[minNode].next 
            
#             cur = cur.next 
            
        
#         return res.next
        
                    
                               

# listofmerge =mergeKListsiteration(listofLink)
# while  listofmerge:
#     print(listofmerge.val)
#     listofmerge= listofmerge.next 
    














#==========================================================================================================================
#                            TWO joint node approach approaach
#==========================================================================================================================






# def mergeKListsTwoJoint( lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#     def mergetwolist(l1,l2):
#         dummy = ListNode()
#         curr= dummy
        
#         while l1 and l2:
#             if l1.val < l2.val:
#                 curr.next = l1
#                 l1 = l1.next
          
#             else:
#                 curr.next = l2
#                 l2 = l2.next
            
#             curr = curr.next
        
#         if l1:
#                curr.next= l1 
#         if l2:
#             curr.next = l2  
                
        
#         return dummy.next  
         
#     if len(lists) == 0:
#             return None

#     for i in  range(1,len(lists)):
#         lists[i]= mergetwolist(lists[i-1],lists[i])
    
#     return lists[-1]
    
    
    
                        
                               

# listofmerge =mergeKListsTwoJoint(listofLink)
# while  listofmerge:
#     print(listofmerge.val)
#     listofmerge= listofmerge.next 







def mergeKListsTwoJointOtherWAy( lists: List[Optional[ListNode]]) -> Optional[ListNode]:

    def mergetwolist(l1,l2):
        dummy = ListNode()
        curr= dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next      
            else:
                curr.next = l2
                l2 = l2.next
                        
            curr = curr.next
        
        if l1:
               curr.next= l1 
        if l2:
            curr.next = l2  
                
        
        return dummy.next  
         
    if len(lists) == 0:
            return None
         
    mergeList = []
    for i in  range(0,len(lists)):
        list1 =  lists[i]      
        list2 =  lists[i+1] if i+1 < len(lists) else None
        mergeList.append(mergetwolist(list1,list2))
    
    return mergeList[0]
                        
listofmerge =mergeKListsTwoJointOtherWAy(listofLink)
while  listofmerge:
    print(listofmerge.val)
    listofmerge= listofmerge.next   