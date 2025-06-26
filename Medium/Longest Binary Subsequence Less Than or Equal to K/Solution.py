class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        n = len(s)

        zero_count = [0] * n

        c = 0

        for i in range(n):
            zero_count[i] = c
            if s[i] == '0':
                c += 1
        

        l = r = n - 1
        res = 0
        while l >= 0:
            while  l >=0 and int(s[l:r+1] , 2) <= k :
                res = max(res,zero_count[l] + r - l + 1)
                l -= 1
            
            r -= 1
            l = min(l,r)
        
        return res

            
        