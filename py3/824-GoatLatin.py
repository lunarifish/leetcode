# 2022-04-21 13:24:28
# Runtime 40ms(38.9%)
# Memory 15mb(23.7%)

##
# Imaa peaksmaaa oatGmaaaa atinLmaaaaa
###

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        new = list()
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for index, i in enumerate(sentence.split(" ")):
            if i[0] in vowels:
                new.append(i + "ma" + "a" * (index + 1))
            else:
                new.append(i[1:] + i[0] + "ma" + "a" * (index + 1))
        return " ".join(new)
