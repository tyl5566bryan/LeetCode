class Solution(object):
    def findSubstring(self, s, words):
        """
            :type s: str
            :type words: List[str]
            :rtype: List[int]
            """
        if not s or not words:
            return []
        
        len_s, len_w, n = len(s), len(words[0]), len(words)
        required, res = collections.defaultdict(int), []
        
        for word in words:
            required[word] += 1
        
        for i in xrange(0, len_s - n * len_w + 1):
            match = collections.defaultdict(int)
            num_match = 0
            while num_match < n:
                word = s[i+len_w*num_match : i+len_w*(num_match + 1)]
                if required[word] == 0 or match[word] >= required[word]:
                    break
                match[word] += 1
                num_match += 1
                if num_match == n:
                    res.append(i)
        
        return res
