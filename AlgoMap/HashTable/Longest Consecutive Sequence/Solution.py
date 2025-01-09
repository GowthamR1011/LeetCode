class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_count = 0
        
        s = set(nums)
        for i in s:
            count = 1
            if i-1 in s:
                continue
            else:
                j = i+1
                while True:
                    if j in s:
                        j += 1
                        count += 1
                    else:
                        break
                if count > longest_count:
                    longest_count = count
        return longest_count