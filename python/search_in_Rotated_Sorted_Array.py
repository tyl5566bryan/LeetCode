class Solution(object):
    def search(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
        def findMinIndex(nums):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) / 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        left, right = 0, len(nums) - 1
        shift = findMinIndex(nums)
        count = len(nums)
        
        while left <= right:
            mid = ((left + right) / 2 + shift) % count
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = (left + right) / 2 + 1
            else:
                right = (left + right) / 2 - 1
        
        return - 1
