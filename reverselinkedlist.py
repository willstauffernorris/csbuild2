# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """            
        ## need a current pointer to keep track of where I'm at in the list
        current = head
        # print(current.val)
        if head is None:
            return None
        next = current.next
        
        prev = None
        
        ## prev 1
        ## current None
        ## next None
        
        ## iterate through the list until the next is None
        while current is not None:
            next = current.next

            
            # change the next to the prev to reverse the list
            current.next = prev
            # print(current) 
            prev = current

            current = next
        
        # if next is None:
        #     print(next)
            
        # print(current)
        # print(head)
        return prev
