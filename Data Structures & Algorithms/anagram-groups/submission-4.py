class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #12:35
        dic={}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s in dic:
                dic[sorted_s].append(s)
            else:
                 dic[sorted_s]=[s]
        res = []
        for val in dic.values():
            res.append(val)
        return res


