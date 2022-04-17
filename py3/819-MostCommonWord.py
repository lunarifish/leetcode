# 2022-04-17 17:49:25
# Runtime 36ms(82.2%) 
# Memory 14.9mb(85.2%)

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freq = defaultdict(int)
        buffer = ""
        
        cur_max = 0
        ret = ""
        for index, i in enumerate(paragraph):
            if i.isalpha():
                buffer += i
            if (not i.isalpha() or index == len(paragraph) - 1) and buffer:
                buffer = buffer.lower()
                if buffer not in banned:
                    freq[buffer] += 1
                    if freq[buffer] > cur_max:
                        cur_max = freq[buffer]
                        ret = buffer
                else:
                    pass
                buffer = ""
        return ret
