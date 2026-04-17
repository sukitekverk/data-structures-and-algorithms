class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre= [1]*len(nums)
        suf= [1]*len(nums)
        res= []
        count_zeros=0

        for i in range(len(nums)):
            if nums[i]== 0:
                count_zeros+=1
            if i>0: 
                pre[i]= pre[i-1]*nums[i-1]
                suf[i]= suf[i-1]*nums[len(nums)-i]

        if count_zeros>=2:
            return [0]*len(nums)
        else:
            for i in range(len(nums)):
                if count_zeros and nums[i]!= 0:
                    res.append(0)
                else:
                    res.append(pre[i]*suf[len(nums)-1-i])
        return res



        