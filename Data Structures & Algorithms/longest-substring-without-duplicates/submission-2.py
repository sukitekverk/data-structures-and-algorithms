class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leng = 0
        chars = {}
        i = 0
        for j in range(len(s)):
            if s[j] in chars:
                i = max(chars[s[j]]+1,i)

            chars[s[j]]=j
            leng = max(leng, j-i+1)
        return leng
        