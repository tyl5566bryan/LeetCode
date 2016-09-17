class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s): return ""
        
        requiredCount = collections.defaultdict(int)
        for c in t:
            requiredCount[c] += 1
        matchedCount = collections.defaultdict(int)
        
        num_diff = len(requiredCount.keys())
        num_match = 0
        len_s, len_min = len(s), len(s) + 1
        left, right, start = 0, -1, 0
        
        while right < len_s - 1:
            
            while num_match < num_diff and right < len_s - 1:
                right += 1
                if requiredCount[s[right]] == 0:
                    continue
                else:
                    matchedCount[s[right]] += 1
                    if matchedCount[s[right]] == requiredCount[s[right]]:
                        num_match += 1
            
            if num_match == num_diff and right - left + 1 < len_min:
                start, len_min = left, right - left + 1
            
            while left <= right and num_match == num_diff:
                if requiredCount[s[left]] == 0:
                    left += 1
                    continue
                elif requiredCount[s[left]] == matchedCount[s[left]]:
                    if right - left + 1 < len_min:
                        start, len_min = left, right - left + 1
                    num_match -= 1
                matchedCount[s[left]] -= 1
                left += 1
                
        if len_min > len_s:
            return ""
        else:
            return s[start: start + len_min]
                
                        