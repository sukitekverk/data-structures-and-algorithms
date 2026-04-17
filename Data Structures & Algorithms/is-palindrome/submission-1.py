class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=''
        for char in s:
            if ord('a')<= ord(char)<= ord('z'):
                cleaned = cleaned +char
            elif ord('A')<= ord(char)<= ord('Z'):
                cleaned = cleaned +char.lower()
            elif ord('0')<= ord(char)<= ord('9'):
                cleaned = cleaned +char
        i = 0
        j = len(cleaned)-1
        while i<= j:
            if cleaned[i]!= cleaned [j]:
                return False
            i+=1
            j-=1
        return True
            