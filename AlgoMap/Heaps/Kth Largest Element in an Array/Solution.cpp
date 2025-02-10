class Solution {
    public:
        int findKthLargest(vector<int>& nums, int k) {
            make_heap(nums.begin(),nums.end());
            int maxm;
            for(int i=1;i<=k;i++){
                maxm = nums[0];
                pop_heap(nums.begin(),nums.end());
                nums.pop_back();
            }
            return maxm;
            
        }
    };