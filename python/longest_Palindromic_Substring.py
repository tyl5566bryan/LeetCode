class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # preprocess
        if not s:
            return ''
        else:
            t = []
            for c in s:
                t = t + ['#', c]
            t = t + ['#']
        
        #Manacher's algorithm
        p = [0] * len(t)
        center, right = 0, 0
        for i in xrange(1, len(t) - 1):
            i_m = 2 * center - i
            if i >= right:
                p[i] = 0
            else:
                p[i] = min(p[i_m], right - i)
                
            while i + p[i] + 1 < len(t) and i - p[i] - 1 > -1 \
            and t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
            
            if i + p[i] > right:
                center = i
                right = i + p[i]
        
        max_id = 0
        for i in xrange(1, len(t) - 1):
            if p[i] > p[max_id]:
                max_id = i
        
        start = (max_id - p[max_id]) / 2
        maxlen = p[max_id]
        return s[start:start+maxlen]
                
                