# 2022-01-07 22:43
# Runtime 32ms(88.5%)
# Memory N/A(100.0%)

class Solution:               
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        def recu(arr, depth = 0, buffer = ''):
            if depth == len(arr):
                res.append(buffer)
                return
            else:
                for i in range(len(arr[depth])):
                    recu(arr, depth + 1, buffer + arr[depth][i])
                    
        pats = []
        a = ord('a')
        for i in digits:
            i = int(i)
            ini = a + (i - 2) * 3
            if i > 7: 
                ini += 1
            if i != 7 and i!= 9:
                pats.append([chr(j) for j in range(ini, ini + 3)])
            else:
                pats.append([chr(j) for j in range(ini, ini + 4)])
        
        if len(pats) == 1:
            return pats[0]
        elif len(pats) == 0:
            return list()
        
        recu(pats)
        return res
