class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        
        num = len(height)
        left_h = [0] * num
        right_h = [0] * num
        left, right = 0, 0
        
        for i in xrange(num):
            left = max(left, height[i])
            right = max(right, height[num-1-i])
            left_h[i], right_h[num-1-i] = left, right
        
        vol = 0
        for i in xrange(num):
            if height[i] < left_h[i] and height[i] < right_h[i]:
                vol = vol + min(left_h[i], right_h[i]) - height[i]
        
        return vol

