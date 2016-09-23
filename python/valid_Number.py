class Solution(object):
    def isNumber(self, s):
        """
            :type s: str
            :rtype: bool
            """
        invalid, space, sign, digit, dot, exponent = range(6)
        transition_matrix = [[-1,  0,  1,  2,  3, -1],
                             [-1, -1, -1,  2,  3, -1],
                             [-1,  8, -1,  2,  4,  5],
                             [-1, -1, -1,  4, -1, -1],
                             [-1,  8, -1,  4, -1,  5],
                             [-1, -1,  6,  7, -1, -1],
                             [-1, -1, -1,  7, -1, -1],
                             [-1,  8, -1,  7, -1, -1],
                             [-1,  8, -1, -1, -1, -1]]     # spaces can be appended to the end
        state = 0
        for ch in s:
            input = invalid
            if ch.isspace():
                input = space
            elif ch == '+' or ch == '-':
                input = sign
            elif ch.isdigit():
                input = digit
            elif ch == '.':
                input = dot
            elif ch == 'e' or ch == 'E':
                input = exponent
                                                                             
            state = transition_matrix[state][input]
            if state == -1:
                return False

        return state == 2 or state == 4 or state == 7 or state == 8
