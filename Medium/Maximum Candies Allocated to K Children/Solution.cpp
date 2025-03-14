class Solution {
    public:
        bool isPossible(vector<int>& candies, long long k, long long x){
            long long count = 0;
    
            for(long long num:candies){
                count += num / x;
            }
    
            return count >= k;
        }
    
        int maximumCandies(vector<int>& candies, long long k) {
            
            
            long long min = 1, max = accumulate(candies.begin(), candies.end(), 0LL)/k, res = 0,mid;
    
            while(min <= max){
                mid = (min + max) / 2;
    
                if(isPossible(candies,k,mid)){
                    res = mid;
                    min = mid +1;
                }
                else{
                    max = mid - 1;
                }
            }
    
            return res;
        }
    };