class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        n = len(grid)

        self.nums = [(0,0)] * (n * n)
        adj = [(1,0), (0,1), (0,-1), (-1,0)]
        diag = [(1,1), (-1,1), (1,-1), (-1,-1)]

        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                res_adj = 0
                res_diag = 0

                for p,q in adj:
                    x , y = i + p, j + q
                    if 0<= x < n and 0<= y < n:
                        res_adj += grid[x][y]
                
                for p,q in diag:
                    x , y = i + p, j + q
                    if 0<= x < n and 0<= y < n:
                        res_diag += grid[x][y]
                    
                
                self.nums[val] = (res_adj, res_diag)
                



    def adjacentSum(self, value: int) -> int:
        
        return self.nums[value][0]

    def diagonalSum(self, value: int) -> int:
        return self.nums[value][1]


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)