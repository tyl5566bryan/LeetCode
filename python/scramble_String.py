class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2): return False
        if s1 == s2: return True
        
        result = [[[False for j in xrange(len(s2))] for i in xrange(len(s1))] for n in xrange(len(s1) + 1)]
        
        for i in xrange(len(s1)):
            for j in xrange(len(s2)):
                if s1[i] == s2[j]:
                    result[1][i][j] = True
        
        for cur_len in xrange(2, len(s1) + 1):
            for i in xrange(len(s1) - cur_len + 1):
                for j in xrange(len(s2) - cur_len + 1):
                    for k in xrange(1, cur_len):
                        if (result[k][i][j] and result[cur_len-k][i+k][j+k]) or \
                        (result[k][i][j+cur_len-k] and result[cur_len-k][i+k][j]):
                            result[cur_len][i][j] = True
                            break
        
        return result[len(s1)][0][0]


