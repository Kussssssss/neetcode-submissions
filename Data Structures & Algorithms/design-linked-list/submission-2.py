class LinkedList:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.left = LinkedList(0)
        self.right = LinkedList(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, prev, next = LinkedList(val), self.left, self.left.next
        prev.next, next.prev = node, node
        node.next, node.prev = next, prev
        
    def addAtTail(self, val: int) -> None:
        node, prev, next = LinkedList(val), self.right.prev, self.right
        prev.next, next.prev = node, node
        node.next, node.prev = next, prev
        
    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, prev, next = LinkedList(val), curr.prev, curr
            prev.next, next.prev = node, node
            node.next, node.prev = next, prev

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            prev, next = curr.prev, curr.next
            prev.next, next.prev = next, prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)