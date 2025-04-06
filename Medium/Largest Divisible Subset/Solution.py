class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()


        dp = defaultdict(int)
        set_dp = defaultdict(list)
        max_set = []

        
        for i in range(len(nums)):
            set_dp[nums[i]] = [nums[i]]
            dp[nums[i]] = 1
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[nums[j]] > dp[nums[i]]:
                        dp[nums[i]] = dp[nums[j]] + 1
                        set_dp[nums[i]] = set_dp[nums[j]] + [nums[i]]
            if len(max_set) < dp[nums[i]]:
                max_set = set_dp[nums[i]]
        print(dp)
        return max_set
                

