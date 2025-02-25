class Solution {
    public:
        int numOfSubarrays(vector<int>& arr) {
            
            long long int res = 0, pre_sum = 0, odd_sum = 0, even_sum = 0;
    
            for(int i=0;i<arr.size();i++){
                pre_sum += arr[i];
    
                if(pre_sum%2 != 0){
                    res += (i-odd_sum)+1;
                    odd_sum++;
        
                }
                else{
                    res += (i-even_sum);
                    even_sum++;
                }
            }
            
            long long int mod = 1e9+7;
            return res % mod;
        }
    };