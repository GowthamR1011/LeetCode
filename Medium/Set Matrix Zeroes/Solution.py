class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zeros = []
        m, n = len(matrix),len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        

        while zeros:

            r,c = zeros.pop()

            for i in range(m):
                matrix[i][c] = 0
            
            for j in range(n):
                matrix[r][j] = 0

        
