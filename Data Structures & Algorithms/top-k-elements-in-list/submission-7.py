class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_map={}
        for n in nums:
            cnt_map[n]= 1+ cnt_map.get(n,0)

        cnt_arr=[]
        for key, value in cnt_map.items():
            cnt_arr.append([key, value])
        cnt_arr.sort(key = lambda x :x[1])

        res= []
        for i in range(len(cnt_arr)-1, len(cnt_arr)-1-k,-1):
            res.append(cnt_arr[i][0])
        return res


            
        