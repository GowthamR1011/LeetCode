class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        int m = matrix.size(),n = matrix[0].size();
        int min_m=0,max_m = m-1, min_n = 0, max_n = n-1,i,j;


        while(true){
            for(j=min_n;j<=max_n;j++){
                result.push_back(matrix[min_m][j]);
            }
            if(result.size()< m*n)
                min_m++;
            else
                break;
            
            for(i=min_m;i<=max_m;i++){
                result.push_back(matrix[i][max_n]);
            }
            if(result.size()< m*n)
                max_n--;
            else
                break;

            for(j=max_n;j>=min_n;j--){
                result.push_back(matrix[max_m][j]);
            }
            if(result.size()< m*n)
                max_m--;
            else
                break;

            
            for(i=max_m;i>=min_m;i--){
                result.push_back(matrix[i][min_n]);
            }
              if(result.size()< m*n)
                min_n++;
            else
                break;
        }
    
        return result;
    }
};

// The solution beats 100% of the solutions in time complexity, with 0ms runtime (according to leetcode)