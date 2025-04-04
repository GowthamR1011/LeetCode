class Solution {
    public:
        int longestNiceSubarray(vector<int>& nums) {
            int l = 0, r= 1, res = 1;
            int x = nums[l];
    
            while(r < nums.size()){
                
                while((x ^ nums[r]) != (x + nums[r]) && l<r){
                    x = x ^ nums[l];
                    l++;
                }
    
                x = x ^ nums[r];
                res = max(res,r - l + 1);
            
                r++;
            }
    
            return res;
        }
    };