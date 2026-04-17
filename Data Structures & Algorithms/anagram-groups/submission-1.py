class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for str in strs:
            sorted_s = "".join(sorted(str))
            if sorted_s not in map:
                map[sorted_s] = []
            map[sorted_s].append(str)
        return list(map.values())