class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        

        if k == 1:
            return 0
            
        n = len(weights)
        score = sorted([weights[i] + weights[i+1] for i in range(n-1)])
        

        maxm = sum(score[-k+1:])
        minm = sum(score[:k-1])

        res = maxm - minm


        return res
