class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m={}
        for s in strs:
            sor_s=str(sorted(s))
            if sor_s in m:
                m[sor_s].append(s)
            else:
                m[sor_s]=[s]
        res = []
        for val in m.values():
            res.append(val)
        return res