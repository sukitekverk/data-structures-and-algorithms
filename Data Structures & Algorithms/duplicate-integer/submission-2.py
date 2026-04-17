class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #4:03
        seen= {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num]=1
        return False

        #4:04