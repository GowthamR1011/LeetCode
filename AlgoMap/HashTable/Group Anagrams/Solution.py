from collections import Counter,defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for st in strs:
            key = [0] * 26
            for ch in st:
                key[ord(ch) - ord('a')] += 1

            key = tuple(key)
            result[key].append(st)
        return list(result.values())
           
