class Solution {
    public:
        bool divideArray(vector<int>& nums) {
            map<int,int> counter;
    
            for(auto i:nums){
                counter[i]++;
            }
    
            for(auto& it:counter){
                if(it.second % 2 != 0)
                    return false;
            }
    
            return true;
        }
    
    };