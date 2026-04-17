class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end = len(nums)-1

        while start<=end:
            mid = start+(end-start)//2
            if nums[mid]==target:
                return mid
             
            #target on right
            if (nums[mid]<target and nums[end]>= target) or (nums[end]<nums[mid] and target<=nums[end]):
                start = mid+1
            else: 
                end= mid-1

        return -1