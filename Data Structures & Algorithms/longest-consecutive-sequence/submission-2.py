class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map ={}
        max_n = 0
        for num in nums:
            if num not in map:
                #its and end
                map[num] = map.get(num-1,0)+ 1 + map.get(num+1,0)
                map[num- map.get(num-1,0)] = map[num]
                map[num+ map.get(num+1,0)] = map[num]
                max_n = max( map[num],max_n)
        return max_n

