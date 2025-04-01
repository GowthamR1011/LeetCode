class Solution {
    public:
        long long mostPoints(vector<vector<int>>& questions) {
            int n = questions.size(),pts,brain;
    
            vector<long long> dp(n+1,0);
    
            for(int i = n-1;i>=0;i--){
    
                pts = questions[i][0];
                brain = questions[i][1];
    
                dp[i] = max( dp[i+1] , pts + dp[min(n, i + 1 + brain)]);
            }
    
            return dp[0];
        }
    };