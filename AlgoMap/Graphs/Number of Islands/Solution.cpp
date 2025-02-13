class Solution {
    public:
        int numIslands(vector<vector<char>>& grid) {
            int island = 0, m = grid.size(), n = grid[0].size();
            pair<int,int> p;
            vector<pair<int,int>> stack;
    
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(grid[i][j] == '1'){
                        island++;
                        stack.push_back({i,j});
    
                        while(stack.size() > 0){
                            p = stack.back();
                            stack.pop_back();
                            
                            if(p.first >= 0 && p.first < m && 
                                p.second >=0 && p.second < n && 
                                grid[p.first][p.second] == '1'){
    
                                grid[p.first][p.second] = '*';
                                stack.push_back({p.first+1,p.second});
                                stack.push_back({p.first,p.second+1});
                                stack.push_back({p.first-1,p.second});
                                stack.push_back({p.first,p.second-1});
                            }
                            
    
                        }
                    }
                }
            }
            return island;
    
            
        }
    };