class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        res = 0
        m = {} #char: index
        for j in range(len(s)):
            if s[j] in m:
                i = max(i, m[s[j]] + 1)
            m[s[j]] = j
            res = max(res, j-i+ 1)

        return res




        