# 2022-04-16 05:11
# Runtime 32mb(91.7%)
# Memory 15mb(39.2%)

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        mapper = {'(': ')', '[': ']', '{': '}'}
        stack = list()
        for i in s:
            if i in mapper: 
                stack.append(mapper[i])
            elif i in mapper.values():
                if not stack or stack[-1] != i:
                    return False
                else:
                    stack.pop(-1)
        return False if stack else True
