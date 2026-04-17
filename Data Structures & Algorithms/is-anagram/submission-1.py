class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = [0]*26
        for l in s:
            cnt[ord(l)- ord('a')]+=1
        for l in t:
             cnt[ord(l)- ord('a')]-=1
        return cnt == [0]*26
        