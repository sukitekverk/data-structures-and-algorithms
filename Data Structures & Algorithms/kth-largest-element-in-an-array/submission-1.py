class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def pivot_alg(l,r):
            pivot = nums[r]
            p = l

            for i in range(l,r):
                if nums[i]<= pivot:
                    temp=nums[i]
                    nums[i]= nums[p]
                    nums[p] = temp
                    p+=1
            nums[p], nums[r]=  nums[r], nums[p]

            if len(nums) - p > k:
                return pivot_alg(p+1,r)
            elif len(nums) -p<k:
                return pivot_alg(l,p-1)
            else:
                return pivot

        return pivot_alg(0, len(nums)-1)


        