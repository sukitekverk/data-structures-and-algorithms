class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #map values to count
        cnt_map= {}
        for n in nums:
            cnt_map[n]= 1 + cnt_map.get(n,0)
        
        #sort cnts into buckets
        cnt_arr= [[] for _ in range(len(nums)+1)]
        for n in cnt_map:
            cnt_arr[cnt_map[n]].append(n)
        
        #get top k into res
        res = []
        for i in range(len(cnt_arr)-1,0,-1):
            for num in cnt_arr[i]:
                res.append(num)
            if len(res) == k:
                return res

        