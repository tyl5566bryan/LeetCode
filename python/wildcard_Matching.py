class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        ptr_p, ptr_s, pre_ptr_p, pre_ptr_s = 0, 0, -1, -1
        while ptr_s < len(s):
            if ptr_p < len(p) and (s[ptr_s] == p[ptr_p] or p[ptr_p] == '?'):
                ptr_p += 1
                ptr_s += 1
            elif ptr_p < len(p) and p[ptr_p] == '*':
                ptr_p += 1
                pre_ptr_s, pre_ptr_p = ptr_s, ptr_p
            elif pre_ptr_s != -1:
                pre_ptr_s += 1
                ptr_s = pre_ptr_s
                ptr_p = pre_ptr_p
            else:
                return False
        
        while ptr_p < len(p) and p[ptr_p] == '*':
            ptr_p += 1
        
        return ptr_p == len(p)
    
    
    # DP, but TLE
    # Time: O(m * n)
    # Space: O(m * n)
    def isMatch2(self, s, p):
        
        len_s, len_p = len(s), len(p)
        
        match = [[False for i in xrange(len_p + 1)] for j in xrange(len_s + 1)]
        match[0][0] = True
        
        for j in xrange(1, len_p + 1):
            if p[j-1] == '*':
                match[0][j] = match[0][j-1]
        
        for i in xrange(1, len_s + 1):
            for j in xrange(1, len_p + 1):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    match[i][j] = match[i-1][j-1]
                elif p[j-1] == '*':
                    match[i][j] = match[i][j-1] or match[i-1][j]
        
        return match[len_s][len_p]
        