# 2022-04-21 03:17:35
# Runtime 44ms(31.5%)
# Memory 15.1mb(73.8%)

##
# 烧脑递归
# 但是提示说这道题可以用dp 像下面这样用递归速度确实不快
# 不管先睡觉啦 88
###

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = list()
        def recu(n, s, depth=0):
            if len(s) == n * 2:
                if depth == 0:
                    ret.append(s)
                return
            else:
                if depth > 0 and depth < n:
                    for select, i in enumerate(["(", ")"]):
                        if select:
                            recu(n, s + i, depth - 1)
                        else:
                            recu(n, s + i, depth + 1)
                elif depth == 0:
                    recu(n, s + "(", depth + 1)
                else:
                    recu(n, s + ")", depth - 1)
        recu(n, "")
        return ret


"""---------------------------------------------"""


# 2022-4-21 3:35
# Runtime 32ms(92.7%)
# Memory 15.2mb(45.5%)

##
# 跟着第二个题解小改了一下
# 现在每一种生成都是合法的了 少做了一些无用功
###

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = list()
        def recu(n, s, l=0, r=0):
            if l == n and r == n:
                ret.append(s)
                return
            else:
                if l == n:
                    recu(n, s + ")" * (l - r), n, n)
                else:
                    if l < n:
                        recu(n, s + "(", l + 1, r)
                    if r < l:
                        recu(n, s + ")", l, r + 1)
        recu(n, "")
        return ret
