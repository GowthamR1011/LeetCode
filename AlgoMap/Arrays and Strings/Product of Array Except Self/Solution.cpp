class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();

        vector<int> left(n,1);
        vector<int> right(n,1);
        vector<int> answer;
        for(int i=1; i < n;i++){
            left[i] = left[i-1] * nums[i-1];
            right[n-i-1] = right[n-i] * nums[n-i];
        }

        for(int j=0;j<n;j++){
            answer.push_back(left[j] * right[j]);
        }
        return answer;
    }
};