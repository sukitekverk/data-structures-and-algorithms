class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n]= 1+count.get(n,0)
        array=[]
        for key, value in count.items():
            array.append([key,value])
        array.sort(key = lambda x:x[1])
        print(array)
        res = []
        i = len(array)-1
        while len(res)<k:
            res.append(array[i][0])
            i-=1
        return res


        