# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        def createTree(lookup, pre, ino, ip, ii, num):
            if num == 0 : return None
            else:
                ind = lookup[pre[ip]]
                node = TreeNode(pre[ip])
                length = ind - ii
                node.left = createTree(lookup, pre, ino, ip+1, ii, length)
                node.right = createTree(lookup, pre, ino, ip+1+length, ii+1+length, num-1-length)
            return node
        
        if not preorder or not inorder: return None
        
        pos_lookup = {}
        for pos, val in enumerate(inorder):
            pos_lookup[val] = pos
        return createTree(pos_lookup, preorder, inorder, 0, 0, len(preorder))
