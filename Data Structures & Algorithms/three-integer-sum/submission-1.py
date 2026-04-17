class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        t = 0
        while t <len(nums):    
            if nums[t]>0:
                return res
            i = t+1
            j = len(nums)-1
            while i< j:
                if nums[i]+nums[j] +nums[t]<0:
                    i+=1
                elif nums[i]+nums[j] +nums[t]>0:
                    j-=1
                else: #=0
                    res.append([ nums[i],nums[j],nums[t]])
                    i+=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
            t+=1
            while t< len(nums) and nums[t]== nums[t-1]:
                t+=1
        return res
