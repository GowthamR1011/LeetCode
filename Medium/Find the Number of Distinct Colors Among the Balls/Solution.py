class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        res = []

        colors = {}
        balls = defaultdict(int)
        for b, c in queries:

            if balls[b] == 0:
                balls[b] = c
                if c in colors:
                    colors[c] += 1
                else:
                    colors[c] = 1
            else:

                oldC = balls[b]
                balls[b] = c

                if c in colors:
                    colors[c] += 1
                else:
                    colors[c] = 1
                
                colors[oldC] -= 1

                if colors[oldC] == 0:
                    del colors[oldC]
                
            
            res.append(len(colors))

        return res
            

