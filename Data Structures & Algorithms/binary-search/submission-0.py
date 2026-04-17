class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r=len(nums)-1
        l=0
        while(r>=l):
            i=(r+l)//2
       
            if nums[i]==target:
                return i
            elif nums[i]< target:
                l=i+1
            else:
                r=i-1
        return -1