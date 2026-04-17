class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_min=1
        k_res=max(piles)
        k_max=max(piles)
        
        while k_min<=k_max:
            k=(k_min+k_max)//2
            curr_h=0
            for i in piles:
                curr_h+= math.ceil(i/k)
                #print('k is ', k, ' and curr_h is ', curr_h)
            if curr_h<=h:
                #print('hi')
                k_res=min(k_res,k)
                k_max=k-1
            else:
                k_min=k+1
        return k_res
                


            

