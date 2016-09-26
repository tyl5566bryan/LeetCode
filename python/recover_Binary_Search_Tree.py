# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        stack = [root]
        pre_val, time = float('-inf'), 0
        
        def swapVal(p1, p2):
            temp = p1.val
            p1.val = p2.val
            p2.val = temp
        
        while stack:
            while stack[-1]:
                stack.append(stack[-1].left)
            stack.pop()
            if stack:
                p = stack.pop()
                if p.val < pre_val and time == 0:
                    p_bad = pre_p
                    p_bad_next = p
                    time += 1
                elif p.val < pre_val and time == 1:
                    swapVal(p, p_bad)
                    return
                pre_val = p.val
                pre_p = p
                stack.append(p.right)
        
        swapVal(p_bad, p_bad_next)
        return