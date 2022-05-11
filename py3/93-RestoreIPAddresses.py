# 2022-05-11 12:32:47
# Runtime 44ms(52.8%)
# Memory 15mb(83.6%)

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = list()
        def rerere(s, lastpos=0, dots=0):
            if dots == 3:
                for i in s.split("."):
                    if int(i) not in range(0, 256) or (i[0] == "0" and len(i) > 1):
                        break
                else:
                    ret.append(s)
                return
            else:
                for i in range(1, 4):
                    s_copy = list(s)
                    if lastpos + i < len(s_copy):
                        s_copy.insert(lastpos+i, ".")
                        rerere("".join(s_copy), lastpos+1+i, dots+1)
                    else:
                        return
        rerere(s)
        return ret
