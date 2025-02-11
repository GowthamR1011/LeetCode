class Solution {
    public:
        vector<int> sol;
        vector<vector<int>> res;
        void backtrack(vector<int> nums){
    
            if(sol.size() == nums.size()){
                res.push_back(sol);
                return;
            }
    
            for(auto x:nums){
                if(count(sol.begin(),sol.end(),x) == 0){
                    sol.push_back(x);
                    backtrack(nums);
                    sol.pop_back();
                }
            }
    
        }
        vector<vector<int>> permute(vector<int>& nums) {
            
            backtrack(nums);
            return res;
        }
    };