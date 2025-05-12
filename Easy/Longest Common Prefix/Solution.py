class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        min_length = len(min(strs, key = lambda x:len(x)))
        for i in range(min_length):

            ch = strs[0][i]

            if all([s[i] == ch for s in strs]):
                res += ch
            else:
                break
        
        return res