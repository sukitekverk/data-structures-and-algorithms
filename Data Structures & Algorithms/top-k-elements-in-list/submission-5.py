class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count
        cnt={}
        for num in nums:
            cnt[num]= 1+ cnt.get(num,0)
        lis = list(cnt.items())
        lis.sort(key = lambda x:x[1])
        res = []
        for i in range(len(lis)-1,len(lis)-1-k, -1):
            res.append(lis[i][0])
        return res
        #11:05
        # I made a lot of small errors
            # range starts with the first number! so you must do len(lis)-1!!!!!!!
            # i forgot = in key = lambda
            # i indexed inside the bracket insead of outside lis[i][0] is right not lis[i[0]]
            # variable name consistant

    #day 2
        #I forgot to do -1 in the range increment
        # i forgot the different between .sort and sorted()

#day 3
# forgot to use len(lis for res loop)
#used sorted instead of sort

