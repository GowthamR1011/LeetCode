#include<unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> counter;
        vector<int> result;
        int diff;
        for(int i:nums){
            if(counter.find(i)==counter.end())
                counter[i] = 1;
            else
                counter[i]++;
        }
        auto j = nums.begin();
        for(auto j=nums.begin();j!=nums.end();j++){
            diff = target - *j;

            if(counter.find(diff) !=counter.end()){
                auto it = find(j+1,nums.end(),diff);
                if(it !=nums.end()){
                    result.push_back(j-nums.begin());
                    result.push_back(it-nums.begin());
                    break;
                }
            }
           
             
        }
        return result;
    }
};