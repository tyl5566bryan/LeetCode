class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def isValid(pos, k):
            for i in xrange(1, k):
                if pos[i] == pos[k] or abs(pos[i] - pos[k]) == k - i:
                    return False
            return True
        
        pos = [0 for i in xrange(n + 1)]
        
        cur, res = 1, []
        
        while cur > 0:
            pos[cur] += 1
            while pos[cur] <= n and not isValid(pos, cur):
                pos[cur] += 1
            
            if pos[cur] <= n:
                if cur == n:
                    this_res = ['.'*(pos[i]-1)+'Q'+'.'*(n-pos[i]) for i in xrange(1, n + 1)]
                    res.append(this_res)
                else:
                    cur += 1
                    pos[cur] = 0
            else:
                cur -= 1
        
        return res
        
        