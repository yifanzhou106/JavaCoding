# 给定arr 每副画的作画时间， num 画家的数量每个画家只能连着画一起的画作，求所有画家并行作画需要的最短时间
class Solution:
    # 思路是最后一个画家负责[k...i]的画,前面num-1个画家负责[0...k-1]的画，两者的最大，取最小值
    def printer1(self, arr, num):
        N = len(arr)
        # 辅助数组用来优化后缀和
        postSum = [0 for _ in range(N)]
        postSum[-1] = arr[-1]
        for i in range(N - 2, -1, -1):
            postSum[i] = postSum[i + 1] + arr[i]

        dp = [[0 for _ in range(num + 1)] for _ in range(N)]
        print(postSum)
        for j in range(num + 1):
            dp[0][j] = arr[0]

        for i in range(1, N):
            dp[i][1] = dp[i - 1][1] + arr[i]

        for i in range(1, N):
            for j in range(2, num + 1):
                dp[i][j] = postSum[0]
                for k in range(i, 0, -1):
                    onePrinter = postSum[k] - postSum[i + 1] if i < N - 1 else postSum[k]
                    dp[i][j] = min(dp[i][j], max(dp[k - 1][j - 1], onePrinter))
        return dp[-1][-1]

    # 四边形不等式优化
    def printer2(self, arr, num):
        N = len(arr)
        # 辅助数组用来优化后缀和
        postSum = [0 for _ in range(N)]
        postSum[-1] = arr[-1]
        for i in range(N - 2, -1, -1):
            postSum[i] = postSum[i + 1] + arr[i]

        dp = [[0 for _ in range(num + 1)] for _ in range(N)]
        choose = [[0 for _ in range(num + 1)] for _ in range(N)]
        for j in range(num + 1):
            dp[0][j] = arr[0]

        for i in range(1, N):
            dp[i][1] = dp[i - 1][1] + arr[i]

        for i in range(1, N):
            for j in range(num, 1, -1):
                dp[i][j] = postSum[0]
                down = choose[i - 1][j]
                up = i if j == num else choose[i][j + 1]
                for k in range(max(1, down), min(i + 1, up + 1)):
                    onePrinter = postSum[k] - postSum[i + 1] if i < N - 1 else postSum[k]
                    if max(dp[k - 1][j - 1], onePrinter) < dp[i][j]:
                        dp[i][j] = max(dp[k - 1][j - 1], onePrinter)
                        choose[i][j] = k

        return dp[-1][-1]


so = Solution()
arr = [1, 1, 1, 4, 3]
print(so.printer1(arr, 3))
print(so.printer2(arr, 3))

