class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        
        count = [0 for i in xrange(n + 1)]
        count[0:3] = [1,1,2]
        
        for i in xrange(3, n + 1):
            for j in xrange(i):
                count[i] += count[j]*count[i-1-j]
        
        return count[n]
                
            