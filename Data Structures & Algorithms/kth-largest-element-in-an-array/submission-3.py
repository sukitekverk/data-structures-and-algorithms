class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_pos= len(nums)-k

        def quickpivot(l,r):
            pivot= nums[r] ##forgot this
            p = l

            
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[i],nums[p]= nums[p], nums[i]
                    p+=1
                
            nums[p],nums[r]= nums[r],nums[p]

            if p <k_pos:
                return quickpivot(p+1,r)
            elif p> k_pos:
                return quickpivot(l,p-1)
            else:
                return pivot

        return quickpivot(0, len(nums)-1)


        