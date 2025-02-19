class Solution {
    public:
        int coinChange(vector<int>& coins, int amount) {
            vector<long int> dp(amount+1,INT_MAX);
            dp[0] = 0;
            sort(coins.begin(),coins.end());
            for(int i=1;i<amount+1;i++){
                for(auto coin:coins){
                    if(coin > i)
                        break;
                    dp[i] = min(dp[i],1+dp[i-coin]);
                }
            }
    
            if(dp[amount] < INT_MAX)
                return dp[amount];
    
            return -1;
        }
    };