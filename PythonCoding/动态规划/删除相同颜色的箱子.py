# 删除箱子
# 给定一个数组里面的数字代表不同的颜色
# 每次可以选择连续的相同颜色的k个箱子删除，并得到分数 k*k
# 求可以得到的最大的得分
class Solution:
    # 范围尝试
    def boxScore(self, arr):
        N = len(arr)
        dp = [[[None for _ in range(N)] for _ in range(N)] for _ in range(N)]
        return self.process(arr, 0, N - 1, 0, dp)

    # L是左边界，R是右边界，K是在L前有多少个和arr[L]相等的箱子数量
    # 1. 假设arr[L]与右侧和arr[L]（记作x）和K个相同的箱子优先消除，则剩下的部分就是 f(x,r,0)
    # 2. 假设arr[L]与右侧和arr[L]（记作x）和K个相同的箱子滞后消除，合并成（k+x个相同的箱子）
    # 对于arr中L之后所有和arr[L]相同颜色的箱子（y），优先合并f(x,y,0)再 f(y,R,k+x)
    def process(self, arr, L, R, K, dp):
        if L > R:
            dp[L][R][K] = 0
            return dp[L][R][K]
        if dp[L][R][K]:
            return dp[L][R][K]
        if L == R:
            dp[L][R][K] = (K + 1) * (K + 1)
            return dp[L][R][K]

        while arr[L] == arr[L + 1]:
            L += 1
            K += 1
        # 假设arr[L]与右侧和arr[L]（记作x）和K个相同的箱子优先消除
        res = (K + 1) * (K + 1) + self.process(arr, L + 1, R, 0, dp)
        # 假设arr[L]与右侧和arr[L]（记作x）和K个相同的箱子滞后消除
        for m in range(L + 1, R + 1):
            if arr[L] == arr[m]:
                res = max(res, self.process(arr, L + 1, m - 1, 0, dp) + self.process(arr, m, R, K + 1, dp))
        dp[L][R][K] = res
        return dp[L][R][K]


so = Solution()
boxs = [1, 3, 2, 2, 2, 3, 4, 3, 1]
print(so.boxScore(boxs))
