class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = []
        
        def backtrack(curr):

            if curr > n:
                return
            
            
            res.append(curr)

            i = 0
            while i < 10 and curr*10 + i <= n:

                nex = curr * 10 + i

                backtrack(nex)

                i += 1

            
        
        for i in range(1,10):
            backtrack(i)

        return res