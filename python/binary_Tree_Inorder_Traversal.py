# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Morris Traversal
    def inorderTraversal(self, root):
        res, cur = [], root
        
        while cur:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                    
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    res.append(cur.val)
                    cur = cur.right
        
        return res
            
        
    
    # stack
    def inorderTraversal_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, myStack = [], [root]
        
        while myStack:
            while myStack[-1] is not None:
                myStack.append(myStack[-1].left)
            myStack.pop()
            if myStack:
                cur = myStack.pop()
                res.append(cur.val)
                myStack.append(cur.right)
        
        return res
        
    # recursion
    def inorderTraversal_3(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        