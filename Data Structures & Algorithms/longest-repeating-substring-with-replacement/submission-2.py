class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        cur_max= 0
        res = 0
        i = 0
        for l,c in enumerate(s):
            cnt[c]= cnt.get(c,0) +1
            cur_max = max(cur_max,cnt[c])
            while l-i +1 - cur_max >k:
                cnt[s[i]] -=1
                i +=1
                
            res = max(res, l-i +1)
        return res
            
