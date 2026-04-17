class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_map={}
        for num in nums:
            cnt_map[num]= cnt_map.get(num,0)+1
    
        sor = sorted(cnt_map.items(), key= lambda x : x[1])
        print(sor)
        res= []
        for i in range(len(sor)-1,len(sor)-k-1,-1):
            res.append(sor[i][0])
        return res

        #cnt map to list of vals
        #sort list
        #take last k
        