class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map= {}
        res = 0
        i = 0
        for j in range(len(s)):
            if s[j] in map:
                i = max(map[s[j]]+1, i)
            map[s[j]]=j
            res = max(j-i+1,res)
        return res
