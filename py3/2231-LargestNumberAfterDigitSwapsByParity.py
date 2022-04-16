# 2022-04-16 19:15:32
# Runtime 32ms(93.7%) 
# Memory 14.8mb(98.2%)

class Solution:
    def largestInteger(self, num: int) -> int:
        ret = [""] * len(str(num))
        odd = list()
        even = list()
        odd_index = list()
        even_index = list()
        for index, i in enumerate(str(num)):
            if (ii := int(i)) % 2:
                odd.append(ii)
                odd_index.append(index)
            else:
                even.append(ii)
                even_index.append(index)
        odd = sorted(odd, reverse=True)
        even = sorted(even, reverse=True)
        for index, i in zip(odd_index, odd):
            ret[index] = str(i)
        for index, i in zip(even_index, even):
            ret[index] = str(i)
            
        return int("".join(ret))
