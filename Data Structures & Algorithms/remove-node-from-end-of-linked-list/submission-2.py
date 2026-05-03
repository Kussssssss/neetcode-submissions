# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        count = 1
        temp = head
        while temp.next:
            temp = temp.next
            count += 1
        tg = count - n
        if tg == 0:
            head = head.next
            return head

        i = 1
        prev = head
        while head.next:
            if i == tg:
                prev.next = prev.next.next
                break
            
            prev = prev.next
            i += 1
        
        return head