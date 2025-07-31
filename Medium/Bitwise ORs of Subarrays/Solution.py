class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        curr = {0}

        for x in arr:
            curr = {x | y for y in curr} | {x}
            res |= curr
        
        return len(res)
