class Solution {
    public:
        int orangesRotting(vector<vector<int>>& grid) {
            int m = grid.size(), n = grid[0].size(), minutes = 0, fresh_oranges = 0,x,y;
    
            vector<pair<int,int>> curr,next, movements = {{1,0},{0,1},{-1,0},{0,-1}} ;
    
            vector<vector<pair<int,int>>> stack;
    
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(grid[i][j] == 1)
                        fresh_oranges++;
                    else if(grid[i][j] == 2){
                        curr.push_back({i,j});
                    }
    
                }
            }
    
    
            stack.push_back(curr);
    
            while(!stack.empty()){
    
                curr = stack.back();
                stack.pop_back();
                next = {};
                for(auto p:curr){
                    for(auto move:movements){
                        x = p.first + move.first;
                        y = p.second + move.second;
                        if(x>=0 && y>=0 && x<m && y<n && grid[x][y]==1){
                            grid[x][y] = 2;
                            fresh_oranges--;
                            next.push_back({x,y});
                        }
                    }
                }
    
    
                if(next.size() > 0){
                    stack.push_back(next);
                    minutes++;
                }
            }
    
    
            if(fresh_oranges>0)
                return -1;
            
            return minutes;
    
        }
    };