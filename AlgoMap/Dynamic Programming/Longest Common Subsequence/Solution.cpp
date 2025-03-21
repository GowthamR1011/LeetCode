class Solution {
    public:
        int longestCommonSubsequence(string text1, string text2) {
         int m = text1.length(), n = text2.length();
    
         vector<vector<int>> grid(m+1, vector<int>(n+1,0));
    
         for(int i=1;i<m+1;i++){
            for(int j=1;j<n+1;j++){
                if(text1[i-1] == text2[j-1])
                    grid[i][j] = 1 + grid[i-1][j-1];
                else
                    grid[i][j] = max(grid[i-1][j],grid[i][j-1]);
            }
         }
    
            return grid[m][n];
    
        }
    };