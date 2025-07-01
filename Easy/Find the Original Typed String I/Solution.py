class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        res = 0

        curr = 1
        for i in range(len(word) - 1):

            if word[i] == word[i+1]:
                curr += 1
                continue
            else:
                res += (curr - 1)
                curr = 1


        res += curr - 1
     
        return res + 1
            