class Solution {
    public:
        vector<vector<int>> res;
        vector<int> sol;
        void backtrack(int i,int n, int k){
            if(sol.size() == k){
                res.push_back(sol);
                return;
            }
            
            for(int index=i;index<=n;index++){
                sol.push_back(index);
                backtrack(index+1,n,k);
                sol.pop_back();
            }
    
        }
        vector<vector<int>> combine(int n, int k) {
            backtrack(1,n,k);
            return res;
        }
    };