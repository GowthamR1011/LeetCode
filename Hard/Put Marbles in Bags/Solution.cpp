class Solution {
    public:
        long long putMarbles(vector<int>& weights, int k) {
            long long n = weights.size(), maxm = 0, minm = 0;
    
            vector<int> scores;
    
            for(int i=0;i<n-1;i++){
                scores.push_back(weights[i] + weights[i+1]);
            }
    
            sort(scores.begin(),scores.end());
    
    
            for(int j=0;j<k-1;j++){
                minm += scores[j];
    
                maxm += scores[n-j-2];
            }
    
            return maxm - minm;
        }
    };