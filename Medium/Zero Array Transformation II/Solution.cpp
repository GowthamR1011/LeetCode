class Solution {
    public:
        bool isZero(vector<int>& nums,vector<vector<int>>& queries, int k){
    
            int prev =0, n = nums.size(),l,r,v;
            vector<int> pre_sum(n,0);
        
            for(int i =0;i<k;i++){
                
                l = queries[i][0];
                r = queries[i][1];
                v = queries[i][2];
    
                pre_sum[l] -= v;
                if(r < n-1)
                    pre_sum[r+1] += v;
        
            }
        
            for(int i=0;i<n;i++){
                pre_sum[i] += prev;
                if(nums[i]+pre_sum[i] > 0)
                    return false;
    
                prev = pre_sum[i];
            }
            return true;
        }
    
        int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
            
            int q = queries.size(),low =0, high = q,mid,res = -1;
    
            while(low<=high){
                mid = (low + high) /2 ;
                if(isZero(nums,queries,mid)){
                    res = mid;
                    high = mid-1;
                }
                else
                    low = mid + 1;
            }
    
            return res;
        }
    };