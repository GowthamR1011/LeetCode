class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        maxm = 0

        for i in range(k):
            if s[i] in 'aeiou':
                maxm += 1
        
        count = maxm

        for i in range(k,len(s)):
            
            if s[i] in 'aeiou':
                count += 1
            
            if s[i-k] in 'aeiou':
                count -= 1
            
            maxm = max(maxm,count)
        
        return maxm