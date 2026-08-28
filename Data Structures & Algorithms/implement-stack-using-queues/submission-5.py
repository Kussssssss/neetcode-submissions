class MyStack:

    def __init__(self):
        self.a = deque()

    def push(self, x: int) -> None:
        self.a.append(x)
        for _ in range(len(self.a) - 1):
            self.a.append(self.a.popleft())

    def pop(self) -> int:
        return self.a.popleft()
    
    def top(self) -> int:
        return self.a[0]
    
    def empty(self) -> bool:
        return len(self.a) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()