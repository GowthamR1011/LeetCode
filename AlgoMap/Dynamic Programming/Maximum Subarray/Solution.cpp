class Solution {
    public:
        int maxSubArray(vector<int>& nums) {
            int cur = 0, maxSum = INT_MIN;
    
            for(auto i:nums){
                cur += i;
    
                maxSum = max(maxSum,cur);
                cur = max(cur,0);
            }
    
            return maxSum;
        }
    };