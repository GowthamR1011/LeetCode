class TrieNode:
    def __init__(self):
        self.letters = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.dictionary = TrieNode()

    def addWord(self, word: str) -> None:
        
        d = self.dictionary

        for ch in word:

            if ch not in d.letters:
                d.letters[ch] = TrieNode()
            
            d = d.letters[ch]
        
        d.word = True


    def search(self, word: str) -> bool:
        
        def dfs(ind, node):
            
            words = node
            for i in range(ind,len(word)):

                if word[i] != '.':
                    if word[i] not in words.letters:
                        return False
                    
                    words = words.letters[word[i]]
                
                else:

                    for l in words.letters.values():
                        if dfs(i+1, l):
                            return True

                    return False

            return words.word

        return dfs(0,self.dictionary) 


            

