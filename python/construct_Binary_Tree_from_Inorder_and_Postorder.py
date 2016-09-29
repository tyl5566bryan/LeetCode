# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        def createTree(lookup, post, ino, ip, ii, num):
            if num == 0 : return None
            else:
                ind = lookup[post[ip]]
                node = TreeNode(post[ip])
                length = ii - ind
                node.right = createTree(lookup, post, ino, ip-1, ii, length)
                node.left = createTree(lookup, post, ino, ip-1-length, ii-1-length, num-1-length)
            return node
        
        if not postorder or not inorder: return None
        
        pos_lookup = {}
        for pos, val in enumerate(inorder):
            pos_lookup[val] = pos
        return createTree(pos_lookup, postorder, inorder, len(postorder)-1, len(inorder)-1, len(inorder))
