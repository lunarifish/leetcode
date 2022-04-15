# 2022-4-15 13:50
# Runtime 36ms(76.1%)
# Memory 15mb(35.4%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return head.next
        
        pointer = head
        length = 0
        while not pointer is None:
            length += 1
            pointer = pointer.next
        if length == n:
            return head.next
        pointer = head
        for i in range(length - n - 1):
            pointer = pointer.next
        pointer.next = pointer.next.next
        return head
