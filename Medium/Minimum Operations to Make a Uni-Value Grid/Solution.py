class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        rem = grid[0][0] % x
        values = []
        for row in grid:
            for item in row:
                if item % x != rem:
                    return -1

                values.append(item)

        
        values.sort()
        val = values[ len(values) // 2]
        res = 0

        for row in grid:
            for item in row:
                 res += abs(item-val) // x
                    
        return res



            