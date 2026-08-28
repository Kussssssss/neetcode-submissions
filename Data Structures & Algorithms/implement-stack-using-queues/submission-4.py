class MyStack:

    def __init__(self):
        self.a = []
        self.len = 0

    def push(self, x: int) -> None:
        self.a.append(x)
        self.len += 1

    def pop(self) -> int:
        temp = self.a[-1]
        del self.a[-1]
        self.len -= 1
        return temp
    
    def top(self) -> int:
        return self.a[-1]
    
    def empty(self) -> bool:
        return self.len == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()