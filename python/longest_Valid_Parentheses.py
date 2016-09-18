class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        stack, start_i, tail_i  = [], [-1], [-1]
        
        for i in xrange(0, len_s):
            if stack:
                if stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                    tail_i[len(stack)] = i
                    tail_i.pop()
                    start_i.pop()
                    continue
            stack.append(s[i])
            start_i.append(i)
            tail_i.append(-1)
        
        res, height = 0, len(start_i)
        for i in xrange(0, height):
            if tail_i[i] - start_i[i] > res:
                res = tail_i[i] - start_i[i]
        
        return res

