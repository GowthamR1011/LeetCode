class Solution:
    def isHammingDistance1(self,s,t):

        if len(s) != len(t):
            return False
        
        c = 0
        for i in range(len(s)):

            if s[i] != t[i]:
                c += 1
                if c > 1:
                    return False
        
        return c == 1

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        

        n = len(words)
        dp = [1] * n
 
        idx = {}
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if self.isHammingDistance1(words[j],words[i]) and groups[i] != groups[j] and dp[j] + 1> dp[i]:
                    dp[i] = 1+ dp[j]
                    idx[i] = j
        
        best = 0
        for i in range(n):
            if dp[i] > dp[best]:
                best = i
        
        
        res = []
        while best in idx:
            res.append(words[best])
            best = idx[best]
        
        res.append(words[best])
        
        return res[::-1]

