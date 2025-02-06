class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l=0,r=0,max_w = 0,n_zeros = 0;

        while(r < nums.size()){

            if(nums[r] == 0)
                n_zeros++;

            if(n_zeros>k){
                if(nums[l]==0)
                    n_zeros--;
                l++;
            }

            if(max_w < (r-l+1))
                max_w = r-l+1;
            
            r++;
        }

        return max_w;
    }
};