class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=''
        for c in s:
            if ord('a')<=ord(c.lower())<+ord('z') or ord('0')<=ord(c.lower())<+ord('9'):
                clean = clean + c.lower()
        i = 0
        j = len(clean)-1

        while i<=j:
            if clean[i]!= clean[j]:
                return False
            i+=1
            j-=1
        return True 