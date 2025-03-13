class Solution:
    def maxArea(self, height: List[int]) -> int:
       
        maxm = 0

        left, right = 0 , len(height) -1

        while left < right:
            
            area = min(height[left],height[right]) * (right-left)
            maxm = max(maxm, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxm

