class Solution {
    public:
        long long maximumTripletValue(vector<int>& nums) {
            long  res = 0, hi  = 0, diff = 0; 
    
            for(auto num:nums){
                res = max(res, long(diff * num));
                diff = max(diff, long (hi - num));
                hi = max(hi,long(num));
            }
    
            return res;
        }
    };