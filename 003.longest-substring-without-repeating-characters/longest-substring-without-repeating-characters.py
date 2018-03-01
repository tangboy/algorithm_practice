class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = {}
        ans = 0
        start = 0
        for i, c in enumerate(s):
            if c in d :
                start = max(start, d[c] + 1)
            d[c] = i
            ans = max(ans, i - start + 1)
            
        return ans