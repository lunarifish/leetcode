# 2022-04-22 22:29:10
# Runtime 36ms(68.8%)
# Memory 14.9mb(85.9%)

##
# 又作弊
###

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        aux = [[i[j] for i in matrix][::-1] for j in range(len(matrix))]
        for i in range(len(matrix)):
            matrix[i] = aux[i]
