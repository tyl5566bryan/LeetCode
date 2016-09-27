# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack1, stack2 = [p], [q]
        while stack1:
            while stack1[-1]:
                if not stack2[-1]: return False
                stack1.append(stack1[-1].left)
                stack2.append(stack2[-1].left)
            if stack2[-1]: return False
            
            stack1.pop()
            stack2.pop()
            
            if stack1:
                if not stack2: return False
                p_, q_ = stack1.pop(), stack2.pop()
                if p_.val != q_.val: return False
                stack1.append(p_.right)
                stack2.append(q_.right)
        
        return True
                
            