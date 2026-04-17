class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sufix= [1]* len(nums)
        prefix=  [1]* len(nums)
        res=  [1]* len(nums)

        for i in range(len(nums)):
            if i >0:
                prefix[i]= prefix[i-1]*nums[i-1]
                sufix[len(nums)-1-i]= sufix[len(nums)-i]*nums[len(nums)-i]
        for i in range(len(nums)):
            res[i]= prefix[i]*sufix[i]
        return res



        