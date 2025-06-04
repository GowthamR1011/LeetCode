class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        if numFriends == 1:
            return word
            
        n = len(word)
        max_word_length = n - numFriends + 1

        res = word[:max_word_length]

        for i in range(1,n):

            if word[i:min(i+max_word_length, n)] > res:
                res = word[i:min(i+max_word_length, n)]
        
        return res
        
