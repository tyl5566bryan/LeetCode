class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def composeOneLine(words, start, tail, length, maxWidth):
            num = tail - start - 1
            extra = maxWidth - num - length
            line = []
            for i in xrange(num):
                line.append(words[start + i])
                line.append(" " * (1 + extra/num + (i < extra % num)))
            line.append(words[tail - 1])
            line_str = "".join(line)
            return line_str + " " * (maxWidth - len(line_str))
        
        res = []
        start, line_length = 0, 0
        for i in xrange(len(words)):
            if line_length + i - start + len(words[i]) > maxWidth:
                res.append(composeOneLine(words, start, i, line_length, maxWidth))
                start, line_length = i, 0
            line_length += len(words[i])
        
        last_line = " ".join(words[start:])
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res

