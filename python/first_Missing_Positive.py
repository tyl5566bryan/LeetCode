class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == i + 1 or nums[i] <= 0 or nums[i] > len(nums):
                i += 1
            elif nums[i] != nums[nums[i] - 1]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            else:
                i += 1
        
        for i in xrange(len(nums)):
            if i != nums[i] - 1:
                return i + 1
        
        return len(nums) + 1
        