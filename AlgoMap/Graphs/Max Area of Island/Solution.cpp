class Solution {
    public:
        int maxAreaOfIsland(vector<vector<int>>& grid) {
            int maxArea = 0, area, m = grid.size(),n = grid[0].size();
            vector<pair<int,int>> stack;
            pair<int,int> p;
    
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(grid[i][j] == 1){
                        stack.push_back({i,j});
                        area = 0;
                        while(stack.size() > 0){
                            p = stack.back();
                            stack.pop_back();
                             if(p.first >= 0 && p.first < m && 
                                    p.second >=0 && p.second < n && 
                                    grid[p.first][p.second] == 1){
                                        
                                        area++;
                                        grid[p.first][p.second] = 2;
                                        stack.push_back({p.first+1,p.second});
                                        stack.push_back({p.first,p.second+1});
                                        stack.push_back({p.first-1,p.second});
                                        stack.push_back({p.first,p.second-1});
                                }
                        }
                        maxArea = max(area,maxArea);
                    }    
                }
            }
    
    
            return maxArea;
        }
    };