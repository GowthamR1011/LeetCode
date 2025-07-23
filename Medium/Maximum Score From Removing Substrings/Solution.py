class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        stack = []

        res = 0
        
        if x > y:
            p,q = 'a','b'
        else:
            p,q = 'b','a'
        
        for ch in s:

            if stack and ch == q and stack[-1] == p:
                stack.pop()
                res += x if x > y else y
            else:
                stack.append(ch)
        

        new_str = "".join(stack)
        stack = []
        for ch in new_str:
            if stack and ch == p and stack[-1] == q:
                stack.pop()
                res += y if x > y else x
            else:
                stack.append(ch)
        

        return res

        



