# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        addr = []
        addr.append(head)  

        while head.next:
            if head.next in addr:
                return True
            addr.append(head.next)
            head = head.next
        
        return False

 