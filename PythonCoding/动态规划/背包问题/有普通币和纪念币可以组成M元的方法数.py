# 普通币可以重复用，纪念币只能用一次

class Solution:

    def coinDP(self, n1, n2, m):
        dp1 = [[0 for _ in range(m + 1)] for _ in range(len(n1) + 1)]
        dp2 = [[0 for _ in range(m + 1)] for _ in range(len(n2) + 1)]

        for i in range(len(n1) + 1):
            dp1[i][0] = 1
        for i in range(len(n2) + 1):
            dp2[i][0] = 1

        for i in range(len(n1) - 1, -1, -1):
            for j in range(m + 1):
                dp1[i][j] = dp1[i + 1][j]
                if j >= n1[i]:
                    dp1[i][j] += dp1[i][j - n1[i]]
        print(dp1[0])
        for i in range(len(n2) - 1, -1, -1):
            for j in range(m + 1):
                dp2[i][j] = dp2[i + 1][j]
                if j >= n2[i]:
                    dp2[i][j] += dp2[i + 1][j - n2[i]]
        print(dp2[0])
        res = 0
        for i in range(m + 1):
            res += dp1[0][i] * dp2[0][m - i]
        return res


so = Solution()
n1 = [5, 1, 2]
n2 = [2, 2, 1, 1, 3, 3, 3]

print(so.coinDP(n1, n2, 10))