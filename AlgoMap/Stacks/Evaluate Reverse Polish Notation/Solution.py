class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for tk in tokens:
            if tk == '+':
                value = stack.pop() + stack.pop()
                stack.append(value)
            
            elif tk == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                value = val2 - val1
                stack.append(value)
            
            elif tk == "*":
                value = stack.pop() * stack.pop()
                stack.append(value)
            elif tk == '/':
                den = stack.pop()
                num = stack.pop()
                stack.append(int(num/den))

            else:
                stack.append(int(tk))
                
            
        return stack[0]