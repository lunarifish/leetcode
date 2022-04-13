# 2022-4-12
# Runtime 32ms(93.3%)
# Memory 14.9mb(96.6%)

##
# 虽然但是用手机打出下面这个字典真的很爽
# 要寄了
###

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {"a": ".-",
                 "b": "-...",
                 "c": "-.-.",
                 "d": "-..",
                 "e": ".",
                 "f": "..-.",
                 "g": "--.",
                 "h": "....",
                 "i": "..",
                 "j": ".---",
                 "k": "-.-",
                 "l": ".-..",
                 "m": "--",
                 "n": "-.",
                 "o": "---",
                 "p": ".--.",
                 "q": "--.-",
                 "r": ".-.",
                 "s": "...",
                 "t": "-",
                 "u": "..-",
                 "v": "...-",
                 "w": ".--",
                 "x": "-..-",
                 "y": "-.--",
                 "z": "--.."}
        res = set()
        for word in words:
            buffer = ""
            for char in word:
                buffer += morse[char]
            res.add(buffer)
        return len(res)
