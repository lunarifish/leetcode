# 2022-04-19 23:33:45
# Runtime 1316ms(10.9%)
# Memory 19mb(57.8%)

##
# 10.9%应该是有人用list作弊吧，
# 应该
# 毕竟这个题除了把入栈反过来好像也没有其他解法了
###

class CQueue:

    def __init__(self):
        self.storage = list()
        self.reverse_out = list()

    def appendTail(self, value: int) -> None:
        self.storage.append(value)

    def deleteHead(self) -> int:
        if not self.storage:
            return -1
        while self.storage:
            self.reverse_out.append(self.storage.pop(-1))
        ret = self.reverse_out.pop(-1)
        while self.reverse_out:
            self.storage.append(self.reverse_out.pop(-1))
        return ret


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
