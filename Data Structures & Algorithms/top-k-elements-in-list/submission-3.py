class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #12:41
        #count like {num:cnt}
        cnt={}
        for num in nums:
            if num in cnt:
                cnt[num]+=1
            else:
                cnt[num]=1
        lis = list(cnt.items())
        lis.sort(key= lambda x :x[1])
        res= []
        for i in range(len(lis)-1,len(lis)-k-1,-1):
            res.append(lis[i][0])
        return res

