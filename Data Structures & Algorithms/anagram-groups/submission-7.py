class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} # str to list
        for s in strs:
            sor = str(sorted(s))
            if sor in map:
                map[sor].append(s)
            else:
                map[sor]=[s]

        res = []
        for val in map.values():
            res.append(val)
        return res
