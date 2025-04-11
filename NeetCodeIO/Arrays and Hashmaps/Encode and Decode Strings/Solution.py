class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        
        length = ""
        res = []
        i = 0
        while i < len(s):
            ch = s[i]

            if ch != '#':
                length += ch
                i += 1
            else:
                res.append(s[i+1:i+1+int(length)])
                i += 1 + int(length)
                length = ""

        return res