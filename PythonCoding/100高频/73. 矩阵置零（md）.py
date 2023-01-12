# 给定一个
# m
# x
# n
# 的矩阵，如果一个元素为
# 0 ，则将其所在行和列的所有元素都设为
# 0 。请使用
# 原地
# 算法。

# 先遍历第一行第一列查看是否需要转成0
# 再用第一行和第一列来记录当前行列是否要变成0
# 最后先把除了第一行列的修改成0
# 在通过一开始的bool值修改第一行列
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rowTo0 = False
        colTo0 = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                colTo0 = True
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                rowTo0 = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if rowTo0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if colTo0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

