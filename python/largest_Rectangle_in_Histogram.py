class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        if not heights: return 0
        heights.append(0)
        stack, max_r = [], 0
        for i in xrange(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_r = max(max_r, heights[cur] * width)
            
            stack.append(i)
        
        return max_r
