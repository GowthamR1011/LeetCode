class Solution {
    public:
        int lenLongestFibSubseq(vector<int>& arr) {
            map<int,int> valToidx;
            int n = arr.size(), res=0,diff;
    
            vector<vector<int>> dp(n,vector<int>(n,2));
    
            for(int i=0;i<n;i++)
                valToidx[arr[i]] = i;
    
            
            for(int i=0;i<n;i++ ){
                for(int j=0;j<n;j++){
                    diff = arr[i]-arr[j];
    
                    if(valToidx.count(diff) > 0 && valToidx[diff] < j)
                        dp[i][j] = dp[j][valToidx[diff]] + 1;
                    
                    res = max(res,dp[i][j]);
                }
    
            }
    
            if(res > 2)
                return res;
            
            return 0;
    
        }
    };