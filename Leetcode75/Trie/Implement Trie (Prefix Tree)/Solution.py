class Trie:

    def __init__(self):
        self.words = {}

    def insert(self, word: str) -> None:
        
        di = self.words
        for ch in word:
            if ch not in di:
                di[ch] = {}
            
            di = di[ch]

        di['.'] = '.'


    def search(self, word: str) -> bool:
        
        di = self.words

        for ch in word:
            if ch not in di:
                return False
            di = di[ch]

        return '.' in di

    def startsWith(self, prefix: str) -> bool:
        
        di = self.words

        for ch in prefix:
            if ch not in di:
                return False
            di = di[ch]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)