class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
           
        n = len(questions)
        dp = [0] * (n+1)

        for i in range(n-1,-1,-1):
            pts,brain = questions[i]

            dp[i] = max(pts+dp[min(n,i+1+brain)] , dp[i+1])
 
        return dp[0]
            