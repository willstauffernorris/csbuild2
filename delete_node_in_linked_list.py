# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        '''
        delete a node except tail in a singly linked list
        only have access to that node
        
        '''
        
#         print(node.val)
#         print(node.next)
        # print(type(node))
        
        node.val = node.next.val
        node.next = node.next.next
        # print(node.val)
        
        
        