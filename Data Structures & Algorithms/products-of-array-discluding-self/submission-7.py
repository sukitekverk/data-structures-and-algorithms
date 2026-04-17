class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #each will ahve length of n
        
        pre= [1]*len(nums)
        for i in range(1,len(nums),1): #n-1
            pre [i]= pre[i-1]*nums[i-1]
        post= [1]*len(nums)
        for i in range(len(nums)-2,-1,-1): #n-1
            post [i]= post[i+1]* nums[i+1]
        comb= [1]*len(nums)
        for i in range(len(nums)):
            comb[i]= pre[i] *post[i]
        return comb