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
