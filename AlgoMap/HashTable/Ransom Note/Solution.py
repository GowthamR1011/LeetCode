class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = set(ransomNote)

        for ch in s:
            if ransomNote.count(ch) > magazine.count(ch):
                return False
        
        return True