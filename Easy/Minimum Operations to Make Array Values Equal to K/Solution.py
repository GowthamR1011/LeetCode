class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        max_count = set()
        

        for num in nums:
            if num > k:
                max_count.add(num)
            elif num < k:
                return -1

        return len(max_count) 