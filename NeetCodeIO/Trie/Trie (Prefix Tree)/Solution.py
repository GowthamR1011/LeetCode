class TrieNode:

    def __init__(self):
        self.letters = {}
        self.end = False
    
class PrefixTree:

    def __init__(self):
        self.dictionary = TrieNode()

    def insert(self, word: str) -> None:
        
        words = self.dictionary
        
        for ch in word:
            if ch not in words.letters:
                words.letters[ch] = TrieNode()
            
            words = words.letters[ch]
        
        words.end = True
    


    def search(self, word: str) -> bool:
        
        words = self.dictionary
        
        for ch in word:
            if ch not in words.letters:
                return False
            
            words = words.letters[ch]
        
        return words.end


    def startsWith(self, prefix: str) -> bool:
        
        words = self.dictionary

        for ch in prefix:

            if ch not in words.letters:
                return False
            
            words = words.letters[ch]
        
        return True
        