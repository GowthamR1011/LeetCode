class Solution {
    public:
        string shortestCommonSupersequence(string str1, string str2) {
            int m = str1.length(), n = str2.length(),i,j;
        
             vector<vector<int>> grid(m+1, vector<int>(n+1,0));
        
             for( i=1;i<m+1;i++){
                for( j=1;j<n+1;j++){
                    if(str1[i-1] == str2[j-1])
                        grid[i][j] = 1 + grid[i-1][j-1];
                    else
                        grid[i][j] = max(grid[i-1][j],grid[i][j-1]);
                }
             }
    
            i = m;
            j = n;
            string res = "";
            
            
            while(i>0 && j >0){
                if(str1[i-1] == str2[j-1]){
                    res += str2[j-1];
                    j--;
                    i--;
                }
                else if(grid[i-1][j]<grid[i][j-1]){
                    res += str2[j-1];
                    j--;
                }
                else{
                    res += str1[i-1];
                    i--;
                }
            }
    
            while(i>0){
                res += str1[i-1];
                i--;
            }
            
            while(j>0){
                res += str2[j-1];
                j--;
            }
    
            reverse(res.begin(),res.end());
            return res;
        }
        
    };