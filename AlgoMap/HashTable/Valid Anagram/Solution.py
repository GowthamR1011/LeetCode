from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_t = Counter(t)
        counter_s = Counter(s)

        return counter_t == counter_s