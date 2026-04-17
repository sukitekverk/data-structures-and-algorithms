class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #4:05
        counter = [0] *26
        for c in s:
            counter[ord(c)-ord('a')] +=1
        for c in t:
            counter[ord(c)-ord('a')] -=1
        for el in counter:
            if el!=0:
                return False

        return True

        