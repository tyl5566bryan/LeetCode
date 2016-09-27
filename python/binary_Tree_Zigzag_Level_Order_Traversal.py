# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        res, cur_level, level = [], [root], 1
        
        while cur_level:
            val, next_level = [], []
            
            for node in cur_level:
                val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            if level % 2 == 1:
                res.append(val)
            else:
                res.append(val[::-1])
            
            level += 1
            cur_level = next_level
        
        return res

