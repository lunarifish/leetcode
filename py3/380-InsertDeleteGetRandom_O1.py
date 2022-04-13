# 2022-4-13
# Runtime 612ms(20.6%)
# Memory 50mb(7.1%)

##
# 愿天堂没有getRandom()
###

class RandomizedSet:
    from random import randint

    def __init__(self):
        self.hashmap = {}
        self.list = list()

    def insert(self, val: int) -> bool:
        try:
            self.hashmap[val]
            return False
        except KeyError:
            self.hashmap[val] = len(self.list)
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        try:
            self.list[self.hashmap[val]] = None
            del self.hashmap[val]
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        ret = self.list[randint(0, len(self.list) - 1)]
        while ret is None:
            ret = self.list[randint(0, len(self.list) - 1)]
        return ret
            


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
