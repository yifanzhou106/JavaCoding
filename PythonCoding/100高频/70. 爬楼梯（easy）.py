# 用logn的方法做

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        M = [[1,1],[1,0]]
        res = self.power(M, n-2)
        return 2 * res[0][0] + res[1][0]


    def power(self, M, p):
        tmp = M
        res = [[1,0],[0,1]]
        while p != 0:
            if p & 1 == 1:
                res  = self.metrixMuti(res, tmp)
            tmp = self.metrixMuti(tmp, tmp)
            p = p >> 1
        return res

    def metrixMuti(self, m1, m2):
        res = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2[0])):
                    res[i][j] += m1[i][k] * m2[k][j]
        return res