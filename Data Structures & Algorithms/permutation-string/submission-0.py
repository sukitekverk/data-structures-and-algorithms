class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #check len s1 <= len s2
        #create char array for s1
        #sliding window for s2 see if it matches s1

        if len(s2)< len(s1):
            return False
        
        s1_ar = [0]*26
        s2_ar = [0]*26

        for c in s1:
            s1_ar[ord(c)-ord('a')] +=1
        l=0
        r = 0
        while r< len(s2):
            if r-l >=len(s1):
                s2_ar[ord(s2[l])-ord('a')] -=1
                l+=1
            s2_ar[ord(s2[r])-ord('a')] +=1


            if s1_ar == s2_ar:
                return True
            r+=1
        return False
