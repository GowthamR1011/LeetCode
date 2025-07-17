class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        

        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            curr = num % k
            for prev in range(k):
                dp[prev][curr] = dp[curr][prev] + 1
                res = max(res, dp[prev][curr])

        return res
            