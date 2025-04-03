class Solution {
    public:
        long long maximumTripletValue(vector<int>& nums) {
            long long res =0, hi = 0, diff = 0;
    
            for(long long num:nums){
                res = max(res,diff * num);
                diff = max(diff, hi - num);
                hi = max(hi,num);
            }
    
            return res;
        }
    };