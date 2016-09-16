class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(0,len(nums)):
            num = nums[i]
            res = target - num
            if res not in dict:
                dict[num] = i
            else:
                return [dict[res], i]