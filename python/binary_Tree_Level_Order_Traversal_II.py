# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        res, cur_level = [], [root]
        
        while cur_level:
            next_level, val = [], []
            for n in cur_level:
                val.append(n.val)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            
            res.append(val)
            cur_level = next_level
        
        return res[len(res)-1::-1]
