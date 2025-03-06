class Solution {
    public:
        vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
            map<int,int> counter;
    
            for(int i=0;i<grid.size();i++){
                for(auto j:grid[i])
                    counter[j]++;
            }
    
            vector<int> res[2];
            for(int x=1;x<=grid.size()*grid.size();x++){
                if(counter[x]==0)
                    res[1] = x;
                else if(counter[x] == 2)
                    res[0] = x;
            }
            return res;
        }
    
    };