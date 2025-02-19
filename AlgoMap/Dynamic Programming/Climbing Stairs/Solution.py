class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1

        prev = 1
        curr = 2

        for i in range(1,n-1):
            prev, curr = curr,curr+prev
        
        return curr

      