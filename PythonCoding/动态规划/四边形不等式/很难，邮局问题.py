class Solution:
    # 给定一个arr代表居民房子在x轴上的位置
    # 邮局只能放在居民房子位置，求如果有k个邮局，怎么使得所有居民到邮局的距离最近
    def postOffice1(self, arr, k):
        if len(arr) < 2 or k <= 0:
            return
        # 辅助数组，代表从0到i位置，只有一个邮局的最短距离
        record = self.findRecord(arr)
        N = len(arr)

        # dp[i][j] 代表在0-i范围内有j个邮局的最短距离
        dp = [[0 for _ in range(k + 1)] for _ in range(N)]
        for i in range(N):
            # 在0-i范围内有一个邮局，和record[0][i]同意
            dp[i][1] = record[0][i]

        # dp[0][....]为0，不用填
        # dp[....][0]无意义
        for i in range(1, N):
            # 如果j>=i的时候，代表邮局数量超过居民楼数，距离必为0，所以只要填到i位置
            # 取k+1和i的最小值
            for j in range(2, min(i, k + 1)):
                # 假如0-i上只用一个邮局，值应该是最大的，设为初始值
                dp[i][j] = record[0][i]
                # 0到m-1上有j-1个邮局 + m到i上有一个邮局
                for m in range(i, 0, -1):
                    dp[i][j] = min(dp[i][j], dp[m - 1][j - 1] + record[m][i])
        return dp[-1][-1]

    # 利用四边形不等式优化
    def postOffice2(self, arr, k):
        if len(arr) < 2 or k <= 0:
            return
        record = self.findRecord(arr)
        N = len(arr)

        dp = [[0 for _ in range(k + 1)] for _ in range(N)]

        # choose[i][j] 代表dp[i][j]最优的时候，中间枚举的m的位置
        # 这里因为行列的单调性，我们可以猜 choose[i][j]最优的位置一定在choose[i-1][j] <= choose[i][j] <= choose[i][j+1]
        choose = [[0 for _ in range(k + 1)] for _ in range(N)]
        for i in range(N):
            dp[i][1] = record[0][i]
            # 0..i 说明 m 的右边没有东西choose[i][1] = 0

        for i in range(1, N):
            for j in range(min(i, k), 1, -1):
                # 下限
                down = choose[i - 1][j]
                # 上限，注意右边界
                up = i if j == min(i, k) else choose[i][j + 1]

                dp[i][j] = record[0][i]
                for m in range(max(1, down), min(i + 1, up + 1)):
                    if dp[m - 1][j - 1] + record[m][i] < dp[i][j]:
                        dp[i][j] = dp[m - 1][j - 1] + record[m][i]
                        choose[i][j] = m

        return dp[-1][-1]

    def findRecord(self, arr):
        N = len(arr)
        # recoord[i][j] 代表在i到j范围内只有一个邮局的最少距离
        record = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                # 只有一个邮局的情况下，邮局在最中心就是最优
                # 每次就假设前一个最优解的中心点在(j+i)/2 位置上
                # 新增的距离就是arr[i] - arr[(j+i) >> 1]
                record[i][j] = record[i][j - 1] + arr[j] - arr[(j + i) >> 1]
        return record


so = Solution()
arr = [3, 18, 105, 877, 987, 1003]
print(so.postOffice1(arr, 3))
print(so.postOffice2(arr, 3))
