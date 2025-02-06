class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_w = 0 
        l,r = 0,0

        while r<len(s):
            while s[r] in s[l:r]:
                l+= 1
            max_w = max(max_w,r-l+1)
            r += 1
            
        return max_w