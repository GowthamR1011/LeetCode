class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        l = 0
        r = 0

        while l < len(word1) and r < len(word2):
            res += word1[l] + word2[r]

            l += 1
            r += 1

        if l < len(word1):
            res += word1[l:]
        
        elif r < len(word2):
            res += word2[r:]

        return res
    
''' 
There is simpler solution, that has less number of codes of line using the zip_longest function from itertools library. 
Though it takes less lines to code, the time complexity is higher. Tested out with Leetcode.
'''
