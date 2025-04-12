class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        res = 0
        left_height = [ 0 ] * n
        right_height = [ 0 ] * n
    

        maxm = 0

        for i in range(n):
            left_height[i] = maxm
            maxm = max(height[i],maxm)
        
        maxm = 0
        for i in range(n-1,-1,-1):
            right_height[i] = maxm
            maxm = max(height[i],maxm)

        
        for i in range(n):
            res += max(min(left_height[i], right_height[i]) - height[i], 0)
        return res