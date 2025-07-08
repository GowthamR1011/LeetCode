class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort()
        n = len(events)

        starts = [s for s,_,_ in events]

        dp = [[-1]* n for _ in range(k+1)]

        

        def dfs(i,count):

            if count == 0 or i == n:
                return 0
            
            if dp[count][i] != -1:
                return dp[count][i]
            
            j = bisect_right(starts,events[i][1])

            dp[count][i] = max(dfs(i+1,count), events[i][2] + dfs(j,count - 1))

            return dp[count][i]
        
        return dfs(0,k)

