class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps={}
        for s in strs:
            sorted_s= str(sorted(s))
            if sorted_s in maps:
                maps[sorted_s].append(s)
            else:
                maps[sorted_s]=[s]
        res=[]
        for val in maps.values():
            res.append(val)

        return res
