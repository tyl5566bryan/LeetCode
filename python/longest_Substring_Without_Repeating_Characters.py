class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myDict = {}
        start_id = 0
        max_len = 0
        
        for i in range(0, len(s)):
            if s[i] in myDict:
                if myDict[s[i]] >= start_id:
                    this_len = i - start_id
                    if this_len > max_len:
                        max_len = this_len
                    start_id = myDict[s[i]] + 1
            myDict[s[i]] = i
            
        final_len = len(s) - start_id
        if final_len > max_len:
            max_len = final_len
            
        return max_len
            
                    
