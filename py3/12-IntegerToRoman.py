# 2022-01-06 19:53
# Runtime 48ms(71.6%)
# Memory N/A(100.0%)

class Solution:
    def isInRange(num, rg: List[float]):
        if num >= min(rg) and num < max(rg):
            return True
        else:
            return False
    def check(num, result):
        if num == 0:
            return result
    def intToRoman(self, num: int) -> str:
        result = ''
        r1 = [0.8, 1.0]
        r2 = [0.9, 1.0]
        while True:
            times = num / 1000
            if times >= 1:
                result += 'M' * int(times)
                num -= 1000 * int(times)
            elif Solution.isInRange(times, r2):
                result += 'CM'
                num -= 900
            elif times < 0.9:
                break
        Solution.check(num, result)
        
        while True:
            times = num / 500
            if times >= 1:
                result += 'D'
                num -= 500
            elif Solution.isInRange(times, r1):
                result += 'CD'
                num -= 400
            elif times < 0.8:
                break
        Solution.check(num, result)
        
        while True:
            times = num / 100
            if times >= 1:
                result += 'C' * int(times)
                num -= 100 * int(times)
            elif Solution.isInRange(times, r2):
                result += 'XC'
                num -= 90
            elif times < 0.9:
                break
        Solution.check(num, result)
        
        while True:
            times = num / 50
            if times >= 1:
                result += 'L'
                num -= 50
            elif Solution.isInRange(times, r1):
                result += 'XL'
                num -= 40
            elif times < 0.8:
                break
        Solution.check(num, result)
        
        while True:
            times = num / 10
            if times >= 1:
                result += 'X' * int(times)
                num -= 10 * int(times)
            elif Solution.isInRange(times, r2):
                result += 'IX'
                num -= 9
            elif times < 0.9:
                break
        Solution.check(num, result)
        
        while True:
            times = num / 5
            if times >= 1:
                result += 'V'
                num -= 5
            elif Solution.isInRange(times, r1):
                result += 'IV'
                num -= 4
            elif times < 0.8:
                break
        Solution.check(num, result)
        
        result += 'I' * int(num)
        return result
