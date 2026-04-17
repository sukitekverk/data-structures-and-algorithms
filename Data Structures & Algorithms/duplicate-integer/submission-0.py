class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        valdict= {}
        for n in nums:
            if n in valdict:
                return True
            valdict[n]=0
        return res