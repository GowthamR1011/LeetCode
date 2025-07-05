class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        c = Counter(arr)
        res = -1
        for k in c:

            if c[k] == k:
                res = max(res,k)
        
        return res