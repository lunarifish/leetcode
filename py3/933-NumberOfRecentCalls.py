# 2022-05-06 03:21:58
# Runtime 2164ms(6.0%)
# Memory 20.1mb(5.1%)

##
# 慢
###

class RecentCounter:

    def __init__(self):
        self.l = list()

    def ping(self, t: int) -> int:
        self.l.append(t)
        self.l = [i for i in self.l if i >= t - 3000]
        return len(self.l)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


"""---------------------------------------------"""


# 2022-5-6 03:26
# Runtime 3368ms(5.0%)
# Memory 19.7mb(75.8%)

##
# 史诗级升级（不
###

class RecentCounter:

    def __init__(self):
        self.l = list()

    def ping(self, t: int) -> int:
        self.l.append(t)
        counter = 0
        for i in self.l[::-1]:
            if i >= t - 3000:
                counter += 1
            else:
                break
        return counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
