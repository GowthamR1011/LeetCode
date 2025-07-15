class Solution:
    def isValid(self, word: str) -> bool:
        vowel =  consonant = False

        vowels = set(['a','e','i','o','u'])

        if len(word) <3 :
            return False

        if not word.isalnum():
            return False

        for ch in word:
            if ch.isalpha():
                if ch.lower() in vowels:
                    vowel = True
                else:
                    consonant = True
        
        
            if vowel and consonant:
                return True
        
        return False
        
