# 2022-05-10 02:24:54
# Runtime 68ms(25.7%)
# Memory 20mb(8.0%)

##
# 分析字母频率的时候返回字符串疯狂出错
# 然后换成tuple就好了
# 可能这就是玄学吧
###

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def analyzeFrequency(s):
            ret = [0] * 26
            for i in s:
                ret[ord(i) - ord("a")] += 1
            return tuple(ret)
        
        ret = defaultdict(list)
        for i in strs:
            ret[analyzeFrequency(i)].append(i)
        return list(ret.values())
