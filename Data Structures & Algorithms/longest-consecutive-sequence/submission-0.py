class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m={}
        res = 0
        for n in nums:
            if m.get(n,0)==0: #didn't already see n
                m[n]=m.get(n-1,0)+m.get(n+1,0)+1
                m[n-m.get(n-1,0)] = m[n] #update right and left bounds based on both sides
                m[n+m.get(n+1,0)]= m[n]
                res = max(res, m[n])
        return res


        