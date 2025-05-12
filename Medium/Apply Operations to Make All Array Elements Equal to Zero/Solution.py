class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        operations = [0] * (n + 1)

        prefix_sum = 0

        for i in range(n):

            prefix_sum += operations[i]
            current = nums[i] - prefix_sum

            if current < 0:
                return False
            
            if current > 0:
                if i + k > n:
                    return False
                operations[i + k] -= current
            prefix_sum += current
        
        return True