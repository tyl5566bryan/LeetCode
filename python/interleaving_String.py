class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3): return False
        
        reach = [[False for i in xrange(len(s2) + 1)] for j in xrange(len(s1) + 1)]
        
        for i in xrange(0, len(s1) + 1):
            for j in xrange(0, len(s2) + 1):
                if i == 0 and j == 0:
                    reach[i][j] = True
                elif i == 0:
                    reach[0][j] = reach[0][j-1] and s2[j-1] == s3[j-1]
                elif j == 0:
                    reach[i][0] = reach[i-1][0] and s1[i-1] == s3[i-1]
                else:
                    reach[i][j] = (reach[i-1][j] and s1[i-1] == s3[i+j-1]) or\
                        (reach[i][j-1] and s2[j-1] == s3[i+j-1])

    return reach[len(s1)][len(s2)]


