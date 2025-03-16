class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        c1 = Counter(word1)
        c2 = Counter(word2)

        if c1 == c2:
            return True
        
        for ch in c1:
            if ch not in c2:
                return False
            
        for ch in c2:
            if ch not in c1:
                return False
        return sorted(c1.values()) == sorted(c2.values())

            