class Solution:
#12:56
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res =res + str(len(s)) + '#' +s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            leng = int(s[i:j])
            res.append(s[j+1:j+1+leng])
            i =j+1+leng
        return res