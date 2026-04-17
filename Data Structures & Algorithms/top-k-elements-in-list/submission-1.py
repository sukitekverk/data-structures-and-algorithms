class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #map values to count
        cnt_map= {}
        for n in nums:
            cnt_map[n]= 1 + cnt_map.get(n,0)
        
        #sort cnts into buckets
        cnt_arr= []
        for n in cnt_map:
            cnt_arr.append([cnt_map[n],n])
        
        cnt_arr.sort()
        #get top k into res
        res = []
        for i in range(len(cnt_arr)-1,-1,-1):
            res.append(cnt_arr[i][1])
            if len(res) == k:
                return res

        