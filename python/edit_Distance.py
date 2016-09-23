class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        distance = [[0 for i in xrange(len2 + 1)] for j in xrange(len1 + 1)]
        
        for i in xrange(1, max(len1, len2) + 1):
            if i <= len1:
                distance[i][0] = i
            if i <= len2:
                distance[0][i] = i
        
        for i in xrange(1, len1 + 1):
            for j in xrange(1, len2 + 1):
                insert = distance[i][j-1] + 1  # insert a char to match j-th char of word2
                delete = distance[i-1][j] + 1  # delete i-th char of word1
                if word1[i-1] != word2[j-1]:   # replace i-th char or not
                    replace = distance[i-1][j-1] + 1
                else:
                    replace = distance[i-1][j-1]
                distance[i][j] = min(insert, delete, replace)
        
        return distance[len1][len2]
