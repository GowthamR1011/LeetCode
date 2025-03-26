class Solution {
    public:
        int minOperations(vector<vector<int>>& grid, int x) {
            int rem = grid[0][0] % x, res = 0,val;
            vector<int> values;
            
            for(auto row:grid){
                for(auto item:row){
                    if(item % x != rem)
                        return -1;
                    
                    values.push_back(item);
                }
            }
    
            sort(values.begin(),values.end());
            val = values[values.size() / 2];
            for(auto item:values){
                res += abs(val - item) / x;
            }
    
            return res;
    
    
        }
    };