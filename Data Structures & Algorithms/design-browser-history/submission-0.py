class LinkedList:

    def __init__(self, name: str = 0):
        self.name = name
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = LinkedList(homepage)
        self.curr = self.home

    def visit(self, url: str) -> None:
        node = LinkedList(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node

    def back(self, steps: int) -> str:
        while self.curr and steps > 0:
            if self.curr.prev == None:
                return self.curr.name
            self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.name
        
    def forward(self, steps: int) -> str:
        while self.curr and steps > 0:
            if self.curr.next == None:
                return self.curr.name
            self.curr = self.curr.next
            steps -= 1

        return self.curr.name


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)