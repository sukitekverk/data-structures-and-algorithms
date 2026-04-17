class Solution:

    def encode(self, strs: List[str]) -> str:
        res= ""
        for s in strs:
            res+= str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l=0
        r=0
        while l<=r and r<len(s):
            if s[r]== '#':
                num = int(s[l:r])
                res.append(s[r+1 : r+1+num])
                l= r+1+num  
                r=l
            else:
                r+=1       

        return res

