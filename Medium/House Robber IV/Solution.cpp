class Solution {
    public:
        bool isPossible(vector<int>&nums,int target,int k){
            int count = 0,i=0;
    
            while(i<nums.size()){
                if(nums[i] <= target){
                    count++;
                    i++;
                    if(count == k)
                        return true;
                }
                i++;
            }
    
            return false;
        }
    
        int minCapability(vector<int>& nums, int k) {
            
            int l = *min_element(nums.begin(),nums.end()), r = *max_element(nums.begin(),nums.end()), target;
    
    
            while(l<=r){
                target = (l + r ) /2 ;
    
                if(isPossible(nums,target,k)){
                    r = target - 1;
                }
                else
                    l = target + 1;
            }
    
            return l;
        }
    };