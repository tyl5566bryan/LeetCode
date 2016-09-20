class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur, reach = 0, 0
        steps = [0] * len(nums)
        
        while reach < len(nums) - 1:
            if cur + nums[cur] >= len(nums) - 1:
                return steps[cur] + 1
            elif cur + nums[cur] > reach:
                steps[reach + 1: cur + nums[cur] + 1] = [steps[cur] + 1] * (cur + nums[cur] - reach)
                reach = cur + nums[cur]
            cur += 1
        
        return 0