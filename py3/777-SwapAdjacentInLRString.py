# 2022-04-29 20:11:32
# Runtime 36ms(100.0%)
# Memory 15mb(94.0%)

##
# 参考了题解的思路
###

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if "".join([i for i in start if i != "X"]) != "".join([i for i in end if i != "X"]):
            return False
        
        encounterR = 0
        encounterL = 0
        for i, j in zip(start, end):
            if j == "L":
                encounterL += 1
            if i == "R":
                encounterR += 1 
                
            if j == "R":
                if encounterR:
                    encounterR -= 1
                else:
                    return False
            if i == "L":
                if encounterL:
                    encounterL -= 1
                else:
                    return False
                
        return True
