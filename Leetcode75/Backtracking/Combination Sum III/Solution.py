class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        curr, res = [],[]

        def backtrack(i):
            
            s = sum(curr)
            if s > n:
                return 
            if s ==  n and len(curr) == k:
                res.append(curr[:])
                return 
            
            for j in range(i,10):
                curr.append(j)
                backtrack(j+1)
                curr.pop()
        
        backtrack(1)
        return res