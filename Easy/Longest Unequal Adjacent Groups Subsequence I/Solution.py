class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        g = [groups[0]]
        res = [words[0]]
        for i in range(1,len(groups)):

            if g[-1] != groups[i]:
                res.append(words[i])
                g.append(groups[i])

            
        return res
            

            

