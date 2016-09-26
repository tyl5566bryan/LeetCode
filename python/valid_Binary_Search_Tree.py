# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre, stack = float('-inf'), [root]
        
        while stack:
            while stack[-1]:
                stack.append(stack[-1].left)
            stack.pop()
            if stack:
                p = stack.pop()
                if p.val <= pre: 
                    return False
                else:
                    pre = p.val
                stack.append(p.right)
        
        return True
                        