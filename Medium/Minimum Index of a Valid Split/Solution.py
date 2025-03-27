class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        counter = defaultdict(int)
        max_count, max_element = 1, nums[0] 
        n = len(nums)
        for num in nums:
            counter[num] += 1
            
            if counter[num] > max_count:
                max_count = counter[num]
                max_element = num

        low_count = 0
        for i in range(n - 1):

            if nums[i] == max_element:
                max_count -= 1
                low_count += 1
            
            if low_count > (i+1)//2 and max_count > (n - 1 - i) // 2:
                return i
        
        return -1


            