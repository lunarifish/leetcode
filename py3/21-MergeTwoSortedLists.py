# 2022-4-14 17:29
# Runtime 44ms(38.2%)
# Memory 14.9mb(75.1%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            pass
        
        ret = ListNode()
        rnext = ret
        
        notdone = list()
        while True:
            try:
                list1.val
            except AttributeError:
                notdone.append(2)
            try:
                list2.val
            except AttributeError:
                notdone.append(1)
            if notdone:
                break
            if list1.val >= list2.val:
                rnext.next = ListNode(list2.val)
                list2 = list2.next
            else:
                rnext.next = ListNode(list1.val)
                list1 = list1.next
            rnext = rnext.next
            
        rnext.next = eval(f"list{notdone[0]}")
        
        return ret.next
