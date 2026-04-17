class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr_max = 0
        i = 0
        j = len(heights)-1

        while i <j:
            vol = min(heights[j],heights[i])*(j-i)
            curr_max = max(curr_max,vol)
            if heights[j]<heights[i]:
                j-=1
            else:
                i+=1
        return curr_max
