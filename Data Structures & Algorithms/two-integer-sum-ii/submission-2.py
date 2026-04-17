class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r= len(numbers)-1
        while r>l:
            s= numbers[r]+numbers[l]
            if s==target:
                return [1+l,1+r]
            elif s<target:
                l+=1
            else:
                r-=1
            