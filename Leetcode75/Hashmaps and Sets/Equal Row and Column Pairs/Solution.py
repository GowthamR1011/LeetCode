class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rows = Counter([tuple(row) for row in grid])
        cols = Counter([tuple([grid[i][j] for i in range(len(grid))]) for j in range(len(grid))])

        count = 0
        for row in rows:
            if row in cols:
                count += rows[row] * cols[row]
        
        return count