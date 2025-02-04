class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1 
        high = num - 1
        if num == 1:
            return True
        while low<=high:
            mid = (low+high) //2

            if num / mid == mid:
                return True
            
            if num / mid > mid:
                low = mid + 1
            else:
                high = mid - 1

        return False