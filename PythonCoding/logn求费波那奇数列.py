class Solution:
    def f(self, N):
        base = [[1, 1], [1, 0]]
        res = self.matrixPower(base, N - 2)
        return res[0][0] + res[1][0]

    def matrixPower(self, m, n):
        res = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
        for i in range(len(res)):
            res[i][i] = 1
        tmp = m

        while n != 0:
            if n & 1 != 0:
                res = self.multMatrix(res, tmp)
            tmp = self.multMatrix(tmp, tmp)
            n = n >> 1
        return res

    def multMatrix(self, m1, m2):
        res = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    res[i][j] += m1[i][k] * m2[k][j]
        return res


so = Solution()
print(so.f(5))