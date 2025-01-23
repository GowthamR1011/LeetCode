class Solution:
    def trap(self, height: List[int]) -> int:
        max_l , max_r = 0,0
        n = len(height)
        left, right = 0, n - 1
        trapped_water = 0

        while left < right:

            if height[left] < height[right]:
               
                if height[left] < max_l:
                    trapped_water +=  max_l - height[left]
                else:
                    max_l = height[left]
                
                left += 1
            
            else:
                
                if height[right] < max_r:
                    trapped_water += max_r - height[right]
                else:
                    max_r = height[right]
                
                right -=1 
            
    
            
        return trapped_water

