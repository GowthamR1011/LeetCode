class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            d = [0] * 26
            for ch in s:
                d[ord(ch) - ord('a')] += 1
            
            d = tuple(d)
            if d in res:
                res[d].append(s)
            else:
                res[d] = [s]
        return res.values()
