class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largestRectangleArea(heights):
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
        
        if not matrix: return 0
        accum = [0 for i in xrange(len(matrix[0]))]
        max_m = 0
        
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                cur_num = ord(matrix[i][j]) - 48
                accum[j] = accum[j] * cur_num + cur_num
            max_m = max(max_m, largestRectangleArea(accum))
        
        return max_m



