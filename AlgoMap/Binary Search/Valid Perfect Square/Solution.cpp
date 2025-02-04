class Solution {
public:
    bool isPerfectSquare(int num) {
        long low = 1, high = num-1 , mid;

        if(num == 1)
            return true;

        while(low<=high){
            mid = (low+high)/2;
            if(num == mid* mid)
                return true;
            
            if(num > mid * mid)
                low = mid + 1;
            else
                high = mid -1;
        }
        return false;
    }
};