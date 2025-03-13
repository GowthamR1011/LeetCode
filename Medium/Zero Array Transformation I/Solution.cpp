class Solution {
    public:
        bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
            int prev =0, n = nums.size();
            vector<int> pre_sum(n,0);
    
            for(auto q:queries){
                pre_sum[q[0]]--;
    
                if(q[1] < n-1)
                    pre_sum[q[1]+1]++;
    
            }
    
            for(int i=0;i<n;i++){
                pre_sum[i] += prev;
    
                if(nums[i]+pre_sum[i] > 0)
                    return false;
    
                prev = pre_sum[i];
            }
    
            return true;
        }
    };