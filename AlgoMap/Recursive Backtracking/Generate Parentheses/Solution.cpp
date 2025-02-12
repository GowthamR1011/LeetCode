class Solution {
    public:
        vector<string> result;
        string sol;
        void backtrack(int index,int n){
            if(sol.size() == 2*n){
                result.push_back(sol);
                return;
            }
    
            for(int i=index;i<sol.size();i++){
                sol.insert(i,"()");
                backtrack(i+1,n);
                sol.erase(i,2);
            }
        }
        vector<string> generateParenthesis(int n) {
            if(n>=1){
                sol = "()";
                backtrack(0,n);
            }
                return result;
        }
    };