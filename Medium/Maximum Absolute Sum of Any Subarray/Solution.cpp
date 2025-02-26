class Solution {
    public:
        int maxAbsoluteSum(vector<int>& nums) {
            int maxSum=nums[0], minSum=nums[0], maxRes=nums[0],minRes=nums[0];
    
            for(int i=1;i<nums.size();i++){
    
                maxSum = max(maxSum+nums[i],nums[i]);
                maxRes = max(maxRes,maxSum);
    
                minSum = min(minSum+nums[i],nums[i]);
                minRes = min(minRes,minSum);
            }
    
            return max(maxRes,abs(minRes));
        }
    };