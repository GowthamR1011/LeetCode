#include<unordered_map>
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> counter;

        for(int i:nums){
            if(counter.find(i) == counter.end()){
                counter[i] = 1;
            }
            else
                counter[i]++;

            if (counter[i] > nums.size() /2 )
                return i;
        }
        return -1;
    }
};