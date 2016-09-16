class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        start_id = 0
        max_len = 0
        
        for i in range(0, len(s)):
            if s[i] in dict:
                if dict[s[i]] >= start_id:
                    this_len = i - start_id
                    if this_len > max_len:
                        max_len = this_len
                    start_id = dict[s[i]] + 1
            dict[s[i]] = i
            
        final_len = len(s) - start_id
        if final_len > max_len:
            max_len = final_len
            
        return max_len
            
                    