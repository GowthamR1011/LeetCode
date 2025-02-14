class Solution {
    public:
        vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
            
            vector<pair<int,int>> movements = {{1,0},{0,1},{0,-1},{-1,0}},stack_a,stack_p;
            int m = heights.size(), n = heights[0].size(),x,y;
            pair<int,int> p;
    
            vector<vector<int>> atlantic_check_grid(m, vector<int>(n, 0)), pacific_check_grid(m, vector<int>(n, 0)), res;
    
    
            for(int i=0;i<m;i++){
                stack_a.push_back({i,n-1});
                atlantic_check_grid[i][n-1] = 1;
    
                stack_p.push_back({i,0});
                pacific_check_grid[i][0] = 1;
            }
    
            for(int j = 0;j<n;j++){
                stack_a.push_back({m-1,j});
                atlantic_check_grid[m-1][j] = 1;
    
                stack_p.push_back({0,j});
                pacific_check_grid[0][j] = 1;
            }
    
            while(!stack_a.empty()){
    
                p = stack_a.back();
                stack_a.pop_back();
    
                for(auto q:movements){
                    x = p.first + q.first;
                    y = p.second + q.second;
    
                    if(x >= 0 && y >=0 && x < m && y < n && heights[x][y] >= heights[p.first][p.second] && atlantic_check_grid[x][y] !=1 ){
                        stack_a.push_back({x,y});
                        atlantic_check_grid[x][y] = 1;
                    }
                }
    
            }
    
    
            while(!stack_p.empty()){
    
                p = stack_p.back();
                stack_p.pop_back(); 
            
                for(auto q:movements){
                    x = p.first + q.first;
                    y = p.second + q.second;
    
                    if(x >= 0 && y >=0 && x < m && y < n && heights[x][y] >= heights[p.first][p.second] && pacific_check_grid[x][y] !=1 ){
                        stack_p.push_back({x,y});
                        pacific_check_grid[x][y] = 1;
                    }
                }
            
            
            }
    
    
            for(int i=0;i<m;i++){
                for(int j =0;j<n;j++){
                    if(atlantic_check_grid[i][j] == 1 &&  pacific_check_grid[i][j] == 1)
                        res.push_back({i,j});
                }
            }
    
            return res;
    
        }
    };