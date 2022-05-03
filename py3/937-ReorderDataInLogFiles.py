# 2022-05-03 13:43:47
# Runtime 32ms(92.7%)
# Memory 15.1mb(65.9%)

##
# python：不愧是我
###

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha = list()
        num = list()
        for i in logs:
            if i.split()[1].isalpha():
                alpha.append(i)
            else:
                num.append(i)
        alpha = sorted(alpha, key=lambda x: x.split()[0])
        alpha = sorted(alpha, key=lambda x: " ".join(x.split()[1:]))
        return alpha + num
