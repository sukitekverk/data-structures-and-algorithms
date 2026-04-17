class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0]*26
        #iterate through s
        for c in s:
            pos = ord(c)-ord('a')
            res[pos] = res[pos]+1
        for c in t:
            pos = ord(c)-ord('a')
            res[pos] = res[pos]-1
        return res== [0]*26

        