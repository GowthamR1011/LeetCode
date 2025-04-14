class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        op_break = {"(" : ")","{" : "}","[":"]"}
        
        for ch in s:

            if ch in op_break:
                stack.append(ch)
            
            elif not stack or op_break[stack.pop()] != ch:
                    return False
        
        return stack == []