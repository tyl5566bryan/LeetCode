# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        stack = [root.left, root.right]
        
        while stack:
            q = stack.pop()
            p = stack.pop()
            
            if not p and not q:
                continue
            
            if not p or not q or p.val != q.val:
                return False
            
            stack.append(p.left)
            stack.append(q.right)
            
            stack.append(p.right)
            stack.append(q.left)
        
        return True

