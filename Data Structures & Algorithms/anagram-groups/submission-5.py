class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #11:10
        map_s= {}
        for s in strs:
            sor= str(sorted(s))
            if sor in map_s:
                map_s[sor].append(s)
            else:
                map_s[sor]= [s]
        res = []
        for val in map_s.values():
            res.append(val)
        return res


        #one small error I forgot to put [] when ititalizing the dict value


