class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        curr_max = 0
        i = 0
        m={} 
        res = 0
        for j in range(len(s)):
            m[s[j]]= m.get(s[j],0)+1
            curr_max = max(curr_max,m[s[j]])
            while (j-i+1) - curr_max >k:
                m[s[i]]-=1
                i+=1
            res = max(res, j-i+1)
        return res




