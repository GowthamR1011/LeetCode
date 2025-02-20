class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s==s[::-1]:
            return s
        
        start = 0
        maxi = 0
        longest_string = ""
        while start < len(s):
            end = len(s) -1 
            while end>=start:
                st = s[start:end+1]
                if st == st[::-1] and maxi < (end-start+1):
                    maxi = end - start + 1
                    longest_string = st
                    break
                
                end -= 1

            start += 1
        return longest_string 