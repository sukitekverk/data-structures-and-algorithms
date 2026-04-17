class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #4:14
        res={}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in res:
                res[sorted_s].append(s)
            else:
                res[sorted_s]=[s]
        res_arr = []
    
        for val in res.values():
            res_arr.append(val)

        return res_arr
        

