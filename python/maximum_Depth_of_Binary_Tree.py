# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        dep = 1
        cur_level = [root]
        
        while cur_level:
            next_level = []
            for n in cur_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            
            if not next_level:
                return dep
            else:
                cur_level = next_level
                dep += 1
                
                