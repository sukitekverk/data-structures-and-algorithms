class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        t = 0
        res = []
        while t<len(nums):
            i = t+1
            j = len(nums)-1
            while i<j:
                if nums[i]+nums[j] > -1*nums[t]:
                    j-=1
                elif nums[i]+nums[j] < -1*nums[t]:
                    i+=1
                else: #==
                    res.append([nums[t],nums[i],nums[j]])
                    i+=1
                    while i<len(nums) and i<j and nums[i] == nums[i-1]:
                        i+=1
            t+=1
            while t<len(nums) and nums[t] == nums[t-1]:
                t+=1
        return res

