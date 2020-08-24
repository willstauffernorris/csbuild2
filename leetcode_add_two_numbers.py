# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        inputs: two non-empty linked lists 
        positive or 0
        single digit
        (2 -> 4 -> 3) + (5 -> 6 -> 4)
        342           +  456         = 
        
        returns:
        807
        (7 -> 0 -> 8)
        
        '''

        print(l1)
        # figure out how to convert a linked list into an int
        
        # convert from LL format to a list
        #iterate through a LL 
        normal_list = []
        normal_list.append(l1.val)
        while l1.next is not None:  
            l1 = l1.next
            normal_list.append(l1.val)
        # print(normal_list)
        
        
        normal_list2 = []
        normal_list2.append(l2.val)
        while l2.next is not None:  
            l2 = l2.next
            normal_list2.append(l2.val)
        # print(normal_list2)
        
        
        # reverse the list
        normal_list.reverse()
        normal_list2.reverse()
#         print(normal_list)
        
        # convert to str and join the pieces together
        ## ideally make this into a function eventually
        new_string = ""
        for element in normal_list:
            element = str(element)
            # print(type(element))
            new_string+=element
            
        new_string2 = ""
        for element in normal_list2:
            element = str(element)
            new_string2+=element
            
        # convert back to int
        new_string = int(new_string)
        new_string2 = int(new_string2)
#         print(new_string)
#         print(new_string2)
        
        # add the two converted LLs (ints)
        new_sum = new_string + new_string2
        # print(new_sum)
        
        # convert this sum back to a list
        new_sum = str(new_sum)
        result_list = []
        for char in new_sum:
            char = int(char)
            result_list.append(char)
                   
        
        # reverse this sum list
        result_list.reverse()
        print(result_list) 
        
        ## convert from a result list back to a LL
        
        
        
        # result_linked_list.val = result_list[0]
        # print(result_linked_list.val)
        
        # for item in result_list:
        #     result_linked_list.val = item
        #     result_linked_list.next
        
        
        # print(l2)
        # i=0
        # while i < len(result_list)-1:
        #     print(i)
        #     result_linked_list = ListNode()
        #     result_linked_list.val = result_list[i]
        #     # result_linked_list.next = ListNode(val=result_list[i+1])
        #     result_linked_list
        #     print(result_linked_list)
        #     i+=1
        #     result_linked_list = result_linked_list.next
        #     print(result_linked_list)
        
#         for item in result_list:
            
#         def lst2link(lst):
#     cur = dummy = ListNode(0)
#     for e in lst:
#         cur.next = ListNode(e)
#         cur = cur.next
#     return dummy.next

        dummy = ListNode(result_list[0])
    
        current = dummy
        
        for item in result_list[1:]:
            current.next = ListNode(item)
            current = current.next
            print(dummy)
            
        print(dummy)
        return dummy
        # print(result_linked_list)
        
        #return this 

        
        
       