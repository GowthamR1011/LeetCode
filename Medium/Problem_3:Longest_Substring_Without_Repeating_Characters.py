'''
Given a string s, find the length of the longest 
substring without repeating characters.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxi = 0 
        for i in range(len(s)):
            end = i

            while end<len(s)-1:
                if s[end+1] in s[i:end+1]:
                    break
                
                end += 1

            if (end - i+1) > maxi:
                maxi = end - i + 1
        
        return maxi
                