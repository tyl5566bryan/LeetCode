class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s, len_p = len(s), len(p)
        match = [[False for j in xrange(len_p + 1)] for i in xrange(len_s + 1)]
        
        match[0][0] = True
        for i in xrange(2, len_p + 1):
            if p[i-1] == '*' and match[0][i-2]:
                match[0][i] = True
        
        for i in xrange(1, len_s + 1):
            for j in xrange(1, len_p + 1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    match[i][j] = match[i-1][j-1]
                if p[j-1] == '*':
                    if p[j-2] != s[i-1] and p[j-2] != '.':
                        match[i][j] = match[i][j-2]
                    else:
                        match[i][j] = match[i][j-2] or match[i][j-1] or match[i-1][j]
        
        return match[len_s][len_p]
        