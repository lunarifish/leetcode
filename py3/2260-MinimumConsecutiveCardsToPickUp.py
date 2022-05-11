# 2022-05-11 19:01:57
# Runtime 156ms(65.6%)
# Memory 33.2mb(81.9%)

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ret = float("inf")
        last_pos = {}
        for index, i in enumerate(cards):
            if i not in last_pos:
                last_pos[i] = index
            else:
                if (cur := index - last_pos[i]) < ret:
                    ret = cur
                last_pos[i] = index
        return ret + 1 if ret != float("inf") else -1
