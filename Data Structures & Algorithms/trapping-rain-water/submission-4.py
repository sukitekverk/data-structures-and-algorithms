class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        left_max =height[0]
        right_max=height[len(height)-1]
        res = 0
        while i <j:
            if height[i]<height[j]:
                i+=1
                left_max=max(left_max,height[i])
                res +=left_max -height[i]
            else:
                j-=1
                right_max=max(right_max,height[j])
                res +=right_max -height[j]
        return res
