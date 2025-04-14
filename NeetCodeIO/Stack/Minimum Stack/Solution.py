class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        
        if not self.stack:
            self.stack.append((val,val))
            return 
        
        minm = min(self.stack[-1][1], val)
        self.stack.append((val,minm))

    def pop(self) -> None:
        _ = self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        
        return self.stack[-1][1]