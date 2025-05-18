class MyStack:

    def __init__(self):
        self.q = deque([])
        self.temp = deque([])

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
    
        while len(self.q) > 1:
            self.temp.append(self.q.popleft())
        self.temp, self.q = self.q, self.temp

        return self.temp.popleft()


    def top(self) -> int:
        
        while len(self.q) > 1:
            self.temp.append(self.q.popleft())
        
        top = self.q.popleft()

        self.temp.append(top)

        self.temp, self.q = self.q, self.temp

        return top

    def empty(self) -> bool:
        
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()