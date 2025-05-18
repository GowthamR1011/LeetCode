class MyQueue:

    def __init__(self):
        self.s = []        

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        temp = []

        while len(self.s) > 1:
            temp.append(self.s.pop())
        
        val =  self.s.pop()

        while len(temp) > 0:
            self.s.append(temp.pop())

        return val

    def peek(self) -> int:
        
        temp = []

        while len(self.s) > 1:
            temp.append(self.s.pop())
        
        val =  self.s.pop()
        temp.append(val)

        while len(temp) > 0:
            self.s.append(temp.pop())
        
        return val
        
    def empty(self) -> bool:
        return len(self.s) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()