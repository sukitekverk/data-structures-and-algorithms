class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #find prod
        zerocnt= 0
        prod=1
        for num in nums:
            if num == 0:
                zerocnt+=1
            else:
                prod*=num
        
        res = [0]*len(nums)
        if zerocnt>1: #more than 1 zero
            return res

        for i,n in enumerate(nums):
            if zerocnt:
                if n==0:
                    res[i]= prod
            else:
                res[i]= prod//n
        return res

        