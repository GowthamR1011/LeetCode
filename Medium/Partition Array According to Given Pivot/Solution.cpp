class Solution {
    public:
        vector<int> pivotArray(vector<int>& nums, int pivot) {
            vector<int> less_than,greater_than,equal ;
    
            for(auto i:nums){
                if(i>pivot)
                    greater_than.push_back(i);
                else if( i < pivot)
                    less_than.push_back(i);
                
                else
                    equal.push_back(i);
            }
    
            less_than.insert(less_than.end(),equal.begin(),equal.end());
            less_than.insert(less_than.end(),greater_than.begin(),greater_than.end());
    
            return less_than;
    
            
        }
    };