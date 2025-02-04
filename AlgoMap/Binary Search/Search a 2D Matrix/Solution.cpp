class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int low_row=0,low_col = 0, high_row = matrix.size() -1, high_col = matrix[0].size() - 1;
        int mid_row,mid_col;
        
        while(low_row<=high_row){
            mid_row = (low_row+high_row) / 2;
            
            if(matrix[mid_row][low_col] <= target && matrix[mid_row][high_col] >= target)
                break;
            
            else if(matrix[mid_row][low_col] > target)
                high_row = mid_row - 1;
            
            else
                low_row = mid_row + 1 ;
        }
        
        if(low_row > high_row)
            return false;
        
        while(low_col<=high_col){
            mid_col = (low_col + high_col) /2;

            if(matrix[mid_row][mid_col] == target)
                return true;
            
            if(matrix[mid_row][mid_col]>target)
                high_col = mid_col - 1;
            else
                low_col = mid_col + 1;
        }
        return false;
    }
};