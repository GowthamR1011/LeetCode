class Solution {
    public:
        vector<int> sol;
        vector<vector<int>> res;
        void backtrack(int index,int target,vector<int> candidates){
    
            if(target < 0)
                return;
            
            if(target == 0){
                res.push_back(sol);
                return;
            }
    
            for(int i=index;i<candidates.size();i++){
                sol.push_back(candidates[i]);
                backtrack(i,target-candidates[i],candidates);
                sol.pop_back();
    
            }
        }
        vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
            backtrack(0,target,candidates);
            return res;
        }
    };