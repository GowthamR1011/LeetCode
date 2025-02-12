class Solution {
    public:
        vector<pair<int,int>> movements;
    
        bool backtrack(int i, int j, int k, int w, int m, int n, vector<vector<char>> &board,string word){
    
            if(board[i][j] != word[k])
                return false;
            
            if(k+1 == w)
                return true;
            
            char ch = board[i][j];
            board[i][j] = '*';
    
            for(auto pair:movements){
                if( i+pair.first >= 0 && i+pair.first < m && j+pair.second >=0 and j+pair.second < n){
                    if(backtrack(i+pair.first,j+pair.second,k+1,w,m,n,board,word))
                        return true;
                }
            }
    
            board[i][j] = ch;
    
            return false;
        }
        bool exist(vector<vector<char>>& board, string word) {
            
            movements.push_back({1,0});
            movements.push_back({-1,0});
            movements.push_back({0,1});
            movements.push_back({0,-1});
    
            int m = board.size(), n= board[0].size(), w = word.size();
    
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(backtrack(i,j,0,w,m,n,board,word)){
                        return true;
                    }
                }
            }
            return false;
    
        }
    };