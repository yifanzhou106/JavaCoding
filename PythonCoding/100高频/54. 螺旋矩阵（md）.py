# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        start = 0
        endX = len(matrix) - 1
        endY = len(matrix[0]) - 1
        res = []
        while start < endX and start < endY:
            for i in range(start, endY):
                res.append(matrix[start][i])
            for j in range(start, endX):
                res.append(matrix[j][endY])
            for i in range(endY, start, -1):
                res.append(matrix[endX][i])
            for j in range(endX, start, -1):
                res.append(matrix[j][start])
            start += 1
            endX -= 1
            endY -= 1

        if start == endY and start < endX:
            while start <= endX:
                res.append(matrix[start][endY])
                start += 1
        elif start == endX and start < endY:
            while start <= endY:
                res.append(matrix[endX][start])
                start += 1
        elif start == endX and start == endY:
            res.append(matrix[endX][start])
        return res
