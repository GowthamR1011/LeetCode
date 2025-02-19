class Solution {
    public:
        bool canJump(vector<int>& nums) {
            int n = nums.size(),i,curr = nums[0];
    
            for(i=0;i<n-1;i++){
                
                curr--;
                curr = max(curr,nums[i]);
    
                if(curr == 0)
                    return false;
            }
    
            return true;
        }
    };