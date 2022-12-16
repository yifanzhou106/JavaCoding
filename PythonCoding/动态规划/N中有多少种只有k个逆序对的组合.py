class Solution:
    # 给定一个N（代表N的所有排列组合）和K（逆序对数量）
    # 求出N里一共有多少种有k个逆序对数量的组合
    # N=3  k=1  有213，一种， k=2 有 231,312两种

    def findCount(self, N, k):
        dp = [[0 for _ in range(k + 1)] for _ in range(N + 1)]
        for i in range(1, N + 1):
            dp[i][0] = 1
        # 以当前数的尾部来做尝试
        # dp[7][5] = dp[6][0] +...+ dp[6][5]
        # dp[6][5]代表7在最后，1-6上已经有5种答案
        # dp[6][0]代表1-6上已经有0种答案，但是7在倒数第6个数字上，后面已经有5个字，总共5种答案
        # 如果j >= i的时候 i-1 上至少需要有j-i+1种逆序对
        # dp[7][9] = dp[6][3] 代表1-6上有3种。7放最前有6种总共9种
        # dp[7][9] = dp[6][9] +...+ dp[6][3]
        for i in range(2, N + 1):
            for j in range(1, k + 1):
                if j >= i:
                    for n in range(j, j - i, -1):
                        dp[i][j] += dp[i - 1][n]
                else:
                    for n in range(j, -1, -1):
                        dp[i][j] += dp[i - 1][n]
        return dp[-1][-1]

    def findCount2(self, N, k):
        dp = [[0 for _ in range(k + 1)] for _ in range(N + 1)]
        for i in range(1, N + 1):
            dp[i][0] = 1
        # 斜率优化一下
        for i in range(2, N + 1):
            for j in range(1, k + 1):
                if j >= i:
                    dp[i][j] = dp[i][j - 1] - dp[i - 1][j - i] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


so = Solution()
print(so.findCount(3, 2))
print(so.findCount(6, 2))
print(so.findCount(8, 9))
print(so.findCount(7, 9))
print(so.findCount(9, 12))

print("***************")
print(so.findCount2(3, 2))
print(so.findCount2(6, 2))
print(so.findCount2(8, 9))
print(so.findCount2(7, 9))
print(so.findCount2(9, 12))