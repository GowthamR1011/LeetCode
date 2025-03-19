class Solution {
    public:
        int minOperations(vector<int>& nums) {
            int count= 0,i;
    
            for( i=0;i<nums.size()-2;i++){
    
                if(nums[i] == 0){
                    count++;
    
                    nums[i]++;
                    nums[i+1] = abs(nums[i+1] - 1);
                    nums[i+2] = abs(nums[i+2] - 1);
                }
            }
    
            if(nums[i] == 1 && nums[i+1] == 1)
                return count;
            
            return -1;
    
        }
    };