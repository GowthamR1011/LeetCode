class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums) - 1

        while l <=r :
            
            m = (l + r) // 2

            if nums[m] == target:
                break
            
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        


        if l > r:
            return [-1, -1]
        l = r =  m
        while 0 <= l and target == nums[l]:
            l -= 1
        

        while r < len(nums) and target == nums[r]:
            r += 1
        

        return [l+1, r -1]