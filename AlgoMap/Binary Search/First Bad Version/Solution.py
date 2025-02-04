# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low = 1
        high = n
        mid = (low+high) // 2
        while isBadVersion(low) != isBadVersion(high):
            mid = (low + high) // 2
            if isBadVersion(mid) != isBadVersion(mid+1):
                return mid+1
            if isBadVersion(mid):
                high = mid - 1
            
            else:
                low = mid + 1
        if isBadVersion(low):
            return low
        
        return high+1
        
