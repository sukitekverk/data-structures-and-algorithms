class Solution:
    def findMin(self, nums: List[int]) -> int:
        r=len(nums)-1
        l=0
        currmin=nums[0]

        while(r>l):
            mid= l+(r-l)//2
        
            currmin=min(currmin,nums[mid]) #possibly mid is min
            if nums[mid]> nums[r] :  #min is to the right
                l=mid+1
            else: # min to to the left
                r=mid-1

        return min(nums[l],currmin)


        