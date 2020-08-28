# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        input: a binary tree
        return max depth
        '''
        
        
        ## OK so I need to traverse through the whole tree. save the first path
        
            # this is the hard part
            
        #I'll do a depth first traversal
        
        # recursion would be good
        
        # def get_neighbors(self, node):
        #     neighbors = []
        #     node.left
       
        ## if there's nothing in the root, the max len is 0
        if not root:
            return 0
        
#         print("LEFT ROOT")
#         print(max(self.maxDepth(root.left)))
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        
        # print(root)
    
        
        ## Go through the rest of the tree. If the current path is longer than the saved longest path, update the saved longest path
        
        # return the len(longest path)
        
        
        