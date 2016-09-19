class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def solver(board):
            for i in xrange(9):
                for j in xrange(9):
                    if board[i][j] == '.':
                        for num in range(1, 10):
                            board[i][j] = chr(num + ord('0'))
                            if checkValid(board, i, j) and solver(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True
            
        def checkValid(board, m, n):
            
            for r in xrange(9):
                if board[r][n] == board[m][n] and r != m:
                    return False
            
            for c in xrange(9):
                if board[m][c] == board[m][n] and c != n:
                    return False
            
            for i in range( (m / 3) * 3, ((m / 3) + 1) * 3):
                for j in range((n / 3) * 3, ((n / 3) + 1) * 3):
                    if board[i][j] == board[m][n] and (i != m or j != n):
                        return False
            
            return True
            
        solver(board)
        
        
        