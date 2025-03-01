class Solution {
    public:
        vector<int> applyOperations(vector<int>& nums) {
            
            for(int i = 0;i<nums.size()-1;i++){
                if(nums[i] == nums[i+1]){
                    nums[i] *= 2;
                    nums[i+1] = 0;
                }
            }
    
            int j = 0,temp;
            for(int k =0;k<nums.size();k++){
                if(nums[k] !=0){
                    temp = nums[k];
                    nums[k] = nums[j];
                    nums[j] = temp;
    
                    j++;
                }
            }
    
            return nums;
    
        }
    };