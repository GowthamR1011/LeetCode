class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:

            if t not in ("+",'-',"*",'/'):
                stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()
            
                if t == "+":    
                    stack.append(int(l+r))
                
                elif t == '-':
                    stack.append(int(l-r))
                
                elif t == '*':
                    stack.append(int(l*r))
                
                elif t == '/':
                    stack.append(int(l/r))

        
        return stack[0]