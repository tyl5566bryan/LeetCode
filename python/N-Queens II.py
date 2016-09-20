class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isValid(pos, k):
            for i in xrange(1, k):
                if pos[i] == pos[k] or abs(pos[i] - pos[k]) == k - i:
                    return False
            return True
        
        pos = [0 for i in xrange(n + 1)]
        
        cur, res = 1, 0
        
        while cur > 0:
            pos[cur] += 1
            while pos[cur] <= n and not isValid(pos, cur):
                pos[cur] += 1
            
            if pos[cur] <= n:
                if cur == n:
                    res += 1
                else:
                    cur += 1
                    pos[cur] = 0
            else:
                cur -= 1
        
        return res