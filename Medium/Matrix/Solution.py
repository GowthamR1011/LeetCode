class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direcs = [(1,0), (0,1), (-1,0) , (0,-1)]

        m,n = len(mat), len(mat[0])

        
        q = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i,j])
                else:
                    mat[i][j] = inf
        

        while q:

            r,c = q.popleft()

            for i,j in direcs:
                x , y = r + i , c + j

                if 0<=x < m and 0<=y<n and mat[x][y] > mat[r][c] + 1:
                    mat[x][y] = mat[r][c] + 1
                    q.append([x,y])    


        return mat 