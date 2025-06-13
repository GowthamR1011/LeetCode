class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()


        def countPairs(threshold):
            n = len(nums)
            count = 0

            i = 0

            while i < n-1:

                if nums[i+1] - nums[i] <=threshold:
                    count += 1
                    i += 1
                
                i += 1

            return count
        

        l, r = 0, nums[-1] - nums[0]

        while l < r :

            mid = (l + r) // 2

            if countPairs(mid) >= p:
                r = mid
            
            else:
                l = mid + 1
            
        
        return r

        

        