class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int i,s=0,max_sum,n=nums.size();

        for(int j=0;j<k;j++)
            s += nums[j];

        max_sum = s;

        for(i=k;i<n;i++){
            s += nums[i] - nums[i-k];
            max_sum = max(max_sum,s);
        }

        return double(max_sum)/k;
    }
};