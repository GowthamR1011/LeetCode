class Solution {
    public:
        int maximumCount(vector<int>& nums) {
            int i = 0, num_zeros = 0, n = nums.size();
    
            while(i<n){
                if(nums[i] > 0)
                    break;
    
                else if(nums[i] == 0)
                    num_zeros++;
                
                i++;
            }   
    
            return max(n-i,i-num_zeros);
        }
    };