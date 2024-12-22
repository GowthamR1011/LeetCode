class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        i = 0

        while True:
            if i == len(strs[0]):
                return strs[0]

            ch = strs[0][i]
            for s in strs[1:]:
                if i== len(s) or ch!=s[i]:
                    return s[:i]
        
            i += 1
        