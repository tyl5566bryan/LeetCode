# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def createTreeRecur(start, end, nums):
            if start > end: return None
            
            mid = (start + end) / 2
            node = TreeNode(nums[mid])
            
            node.left = createTreeRecur(start, mid - 1, nums)
            node.right = createTreeRecur(mid + 1, end, nums)
            
            return node
        
        return createTreeRecur(0, len(nums) - 1, nums)
            