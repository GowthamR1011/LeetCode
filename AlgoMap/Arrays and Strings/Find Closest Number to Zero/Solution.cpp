class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int minimum = abs(nums[0]);
        int x = nums[0];
        for(int i:nums)
        {
            if(abs(i) < minimum || (abs(i) == minimum && x < i))
            {
                minimum = abs(i);
                x = i;
            }
        }

        return x; 
    }
};