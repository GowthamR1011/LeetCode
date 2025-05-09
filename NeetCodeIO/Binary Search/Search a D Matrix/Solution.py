class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l_r, h_r = 0, len(matrix) - 1
        l_c,h_c = 0, len(matrix[0]) - 1
        row = -1
        while l_r <= h_r:

            m = (l_r + h_r) // 2
            
            if matrix[m][0] <= target <= matrix[m][h_c]:
                row= m
                break
            
            elif matrix[m][0] > target:
                h_r = m - 1
            
            else:
                l_r = m + 1
        
        if row == -1:
            return False
        

        while l_c <= h_c:

            m = (l_c + h_c) // 2

            if matrix[row][m] == target:
                return True
            
            if matrix[row][m] > target:
                h_c = m - 1
            else:
                l_c = m + 1
        
        return False

