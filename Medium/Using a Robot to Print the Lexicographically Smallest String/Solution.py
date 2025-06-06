class Solution:
    def robotWithString(self, s: str) -> str:
        
        counter = Counter(s)
        
        res = ""
        stack = []
        minCharacter = "a"
        for ch in s:

            stack.append(ch)

            counter[ch] -= 1

            while minCharacter != "z" and counter[minCharacter] == 0:
                minCharacter = chr(ord(minCharacter) + 1)
            
            while stack and stack[-1] <= minCharacter:
                res += stack.pop()
            
        
        return res

            
