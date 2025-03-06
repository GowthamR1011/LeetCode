class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        counter = defaultdict(int)
        for i in range(len(grid)):
            for num in grid[i]:
                counter[num] += 1
        res = [-1] * 2
        for x in range(1,len(grid)*len(grid)+1):
            if counter[x] == 0:
                res[1] = x
            elif counter[x] == 2:
                res[0] = x
        
        return res