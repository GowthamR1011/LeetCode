class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low_row = 0
        high_row = len(matrix) - 1
        low_col = 0
        high_col = len(matrix[0]) - 1

        while low_row <= high_row:
            mid_row = (low_row + high_row) // 2
            
            if matrix[mid_row][low_col] <= target and matrix[mid_row][high_col] >= target:
                break
            
            elif matrix[mid_row][low_col] > target:
                high_row = mid_row - 1
            
            else:
                low_row = mid_row + 1
        
        if low_row > high_row:
            return False
        
        while low_col<=high_col:
            mid_col = (low_col + high_col) // 2

            if matrix[mid_row][mid_col] == target:
                return True
            
            if matrix[mid_row][mid_col] > target:
                high_col = mid_col - 1

            else:
                low_col = mid_col + 1
        
        return False