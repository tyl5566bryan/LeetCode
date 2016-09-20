class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach, start = 0, 0
        
        while start <= reach and reach < len(nums) - 1:
            reach = max(reach, start + nums[start])
            start += 1
        
        if start > reach:
            return False
        else:
            return True
            
            