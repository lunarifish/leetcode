# 2022-1-3 16:16
# Runtime 316ms(7.3%)
# Memory 15.2mb(5.1%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def readnode(ln):
            l = list()
            while True:
                l = [str(ln.val)] + l
                try:
                    ln = ln.next
                    ln.val
                except:
                    break
            return l
        s1, s2 = list(), list()
        s1 = readnode(l1)
        s2 = readnode(l2)
        val = 0
        for i in [s1, s2]:
            val += int(''.join(i))
        val = str(val)[::-1]
        res = ListNode(int(val[0]))
        for i in range(len(val)):
            exec('res{} = ListNode(int(val[i]))'.format(r'.next' * i))
        return res
