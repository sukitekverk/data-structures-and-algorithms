class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        count = {}
        for n in nums:
            count[n]= count.get(n,0)+1
        lis = []
        for el in count:
            lis.append((el,count[el]))

        lis.sort(key = lambda x:x[1])
        res = []
        for i in range(k):
            res.append(lis[len(lis)-i-1][0])

        return res