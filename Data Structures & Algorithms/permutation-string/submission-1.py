class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        c_s1=[0]*26
        for i in range(len(s1)):
            c_s1[ord(s1[i])-ord('a')]+=1
        
        l= 0
        r=0
        c_s2=[0]*26
        while r<len(s2):
            c_s2[ord(s2[r])-ord('a')]+=1
            if r-l>=len(s1):
                c_s2[ord(s2[l])-ord('a')]-=1
                l+=1
            if c_s1 == c_s2:
                return True
            r+=1
        return False



        