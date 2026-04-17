class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m={}
        res = 0
        for n in nums:
            if n not in m:
                m[n]= m.get(n-1,0)+m.get(n+1,0)+1
                m[n+m.get(n+1,0)]= m[n]
                m[n-m.get(n-1,0)]=m[n]
                res = max(res, m[n])
        return res

            
        