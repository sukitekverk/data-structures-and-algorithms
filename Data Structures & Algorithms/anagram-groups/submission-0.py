class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict= {}
        for s in strs:
            chars= [0]*26
            for c in s:
                chars[ord(c)-ord('a')] +=1
            if tuple(chars) not in res_dict:
                res_dict[tuple(chars)]= []
            res_dict[tuple(chars)].append(s)

        return list(res_dict.values())

