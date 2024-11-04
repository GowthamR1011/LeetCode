#include <vector>
class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> new_list = {};
    for(int num:nums){
        new_list.push_back(nums[num]);
    }
    return new_list;
    }
};