class Solution {
    public:
        vector<int> sol;
        vector<vector<int>> res;
        void backtrack(vector<int> nums,int i,int n){
            if(i==n){
                res.push_back(sol);
                return;
            }
    
            backtrack(nums,i+1,n);
    
    
            sol.push_back(nums[i]);
            backtrack(nums,i+1,n);
            sol.pop_back();
        }
        vector<vector<int>> subsets(vector<int>& nums) {
            
            backtrack(nums,0,nums.size());
            return res;
        }
    };