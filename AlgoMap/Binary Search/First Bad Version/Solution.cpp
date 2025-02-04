// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        double low = 1, high = n, mid;

        while(isBadVersion(low) != isBadVersion(high)){

            mid = (low + high) / 2;

            if(isBadVersion(mid) != isBadVersion(mid+1))
                return mid + 1;
            
            if(isBadVersion(mid))
                high = mid -1 ;
            else
                low = mid + 1;
        }

        if(isBadVersion(low))
            return low;
        
        return high+1;

    }
};