class Solution {
    public:
        int minSubArrayLen(int target, vector<int>& nums) {
            int min_length = INT_MAX, l = 0, r= 0, sum = 0;
            
            while(r<nums.size()){
                sum += nums[r];
    
                while(sum>=target){
                    min_length = min(min_length,r-l+1);
                    sum -= nums[l];
                    l++;
                }
                r++;
            }
    
            if(min_length == INT_MAX)
                return 0;
            else
                return min_length;
        }
    };