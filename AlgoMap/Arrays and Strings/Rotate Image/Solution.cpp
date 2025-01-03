class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size(),i,j,temp;

        for(i=0;i<n;i++){
            for(j=0;j<i;j++){
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        for(i=0;i<n;i++){
            for(j=0;j<n/2;j++){
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][n-j-1];
                matrix[i][n-j-1] = temp;
            }
        }

        
    }
};

//  The solution beats 100% of the solutions in time complexity, with 0ms runtime (according to leetcode)