class Solution:
    def trap(self, height: List[int]) -> int:
        #l......r
        if not height:
            return 0

            
        l = 0
        r = len(height)-1
        leftmax = height[l]
        rightmax = height[r]
        res = 0

        while l<r:
            if leftmax>rightmax:
                r-=1
                rightmax = max(rightmax,height[r])
                res += rightmax-height[r]
            else:
                l+=1
                leftmax = max(leftmax, height[l])
                res += leftmax-height[l]
                
        return res

