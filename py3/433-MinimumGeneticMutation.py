# 2022-05-07 03:10:50
# Runtime 36ms(67.9%)
# Memory 15.1mb(30.0%)

##
# 《题目提示说用bfs但是好像忘记怎么写了那就用dfs吧》
###

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        
        def isValidMutation(s, e): 
            return True if len([i for i in zip(s, e) if i[0] != i[1]]) == 1 else False
        def getValidMutations(s, bank, banned):
            ret = list()
            for i in bank:
                if isValidMutation(s, i) and i not in banned:
                    ret.append(i)
            return ret
        ret = [float("inf")]
        def dfs(s, dst, bank, banned=[], depth=0):
            if s == dst and depth < ret[0]:
                ret[0] = depth
            else:
                for i in getValidMutations(s, bank, banned+[s]):
                    dfs(i, dst, bank, banned+[s], depth+1)
                
        dfs(start, end, bank)
        return ret[0] if ret[0] != float("inf") else -1
