# 2022-4-16 13:50
# Runtime 7452ms(6.7%)
# Memory 16.5mb(5.2%)

class Solution:
    def jump(self, nums: List[int]) -> int:
        def leastStepsFromHere(pos, l, history):
            def recu(output, pos, l, history, depth=0):
                if pos in history:
                    output.append(history[pos] + depth)
                    return
                elif pos == len(l) - 1:
                    output.append(depth)
                    return
                elif l[pos] == 0:
                    output.append(float("inf"))
                    return
                else:
                    for i in range(1, l[pos] + 1):
                        try:
                            recu(output, pos + i, l, history, depth + 1)
                        except IndexError:
                            pass
            
            ret = list()
            recu(ret, pos, l, history)
            return min(ret)

        dpnodes = {}
        for i in range(len(nums))[::-1]:
            cur = leastStepsFromHere(i, nums, dpnodes)
            dpnodes[i] = cur
        return cur
                
