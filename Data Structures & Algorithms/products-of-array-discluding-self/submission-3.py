class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre= [1]*len(nums)
        suf= [1]*len(nums)
        res= []

        for i in range(len(nums)):
            if i>0: 
                pre[i]= pre[i-1]*nums[i-1]
                suf[i]= suf[i-1]*nums[len(nums)-i]
        for i in range(len(nums)):
            res.append(pre[i]*suf[len(nums)-1-i])
        return res



        