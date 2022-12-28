# 整型数组arr长度为(3<=n<=10^4)， 最初的每个数字都是 <=200的正数并满足以下条件：
# 1. arr[0] <= arr[1]
# 2. arr[n-2] <= arr[n-1]
# 3. arr[i] <= max(arr[i-1], arr[i+1])
# 目前arr上面有些数字丢失了，丢失后当前位子值为0
# 根据以上条件，求出有多少种不同的arr可以满足以上条件

class Solution:
    def ways(self, arr):
        N = len(arr)
        if arr[-1] != 0:
            return self.process(arr, N - 1, arr[-1], 2)
        else:
            res = 0
            for i in range(1, 201):
                res += self.process(arr, N - 1, i, 2)
            return res

    # cmp == 0, 当前val小于右
    # cmp == 1, 当前val等于右
    # cmp == 2, 当前val大于右
    def process(self, arr, index, val, cmp):
        if index == 0:
            return 1 if (cmp == 0 or cmp == 1) and (arr[0] == 0 or arr[0] == val) else 0
        if arr[index] != 0 and arr[index] != val:
            return 0

        res = 0
        if cmp == 0 or cmp == 1:
            # 当前位置已经满足条件 arr[i] <= max(arr[i-1], arr[i+1])，可以从1-200任意选择
            for i in range(1, 201):
                nextCmp = 0
                if i == val:
                    nextCmp = 1
                elif i > val:
                    nextCmp = 2
                res += self.process(arr, index - 1, i, nextCmp)
        else:
            # 当前位置不满足条件 arr[i] <= max(arr[i-1], arr[i+1])，只能>=val, 从val-200选择
            for i in range(val, 201):
                nextCmp = 0
                if i == val:
                    nextCmp = 1
                elif i > val:
                    nextCmp = 2
                res += self.process(arr, index - 1, i, nextCmp)
        return res

    def waysDP(self, arr):
        N = len(arr)
        dp = [[[0 for _ in range(3)] for _ in range(201)] for _ in range(N)]

        if arr[0] != 0:
            dp[0][arr[0]][0] = 1
            dp[0][arr[0]][1] = 1
        else:
            for v in range(1, 201):
                dp[0][v][0] = 1
                dp[0][v][1] = 1

        for i in range(1, N):
            for v in range(1, 201):
                for cmp in range(3):
                    res = 0
                    if cmp == 0 or cmp == 1:
                        for k in range(1, 201):
                            nextCmp = 0
                            if k == v:
                                nextCmp = 1
                            elif k > v:
                                nextCmp = 2
                            res += dp[i - 1][k][nextCmp]
                    else:
                        for k in range(v, 201):
                            nextCmp = 0
                            if k == v:
                                nextCmp = 1
                            elif k > v:
                                nextCmp = 2
                            res += dp[i - 1][k][nextCmp]
                    dp[i][v][cmp] = res

        if arr[-1] != 0:
            return dp[N - 1][arr[-1]][2]
        else:
            res = 0
            for i in range(1, 201):
                res += dp[N - 1][i][2]
            return res

            # 斜率优化过

    def waysDP2(self, arr):
        N = len(arr)
        dp = [[[0 for _ in range(3)] for _ in range(201)] for _ in range(N)]

        if arr[0] != 0:
            dp[0][arr[0]][0] = 1
            dp[0][arr[0]][1] = 1
        else:
            for v in range(1, 201):
                dp[0][v][0] = 1
                dp[0][v][1] = 1
        preSum = [[0 for _ in range(3)] for _ in range(201)]
        for v in range(1, 201):
            for cmp in range(3):
                preSum[v][cmp] = preSum[v - 1][cmp] + dp[0][v][cmp]

        for i in range(1, N):
            for v in range(1, 201):
                for cmp in range(3):
                    res = 0
                    if cmp == 0 or cmp == 1:
                        dp[i][v][cmp] += preSum[v - 1][0] - preSum[0][0]
                        dp[i][v][cmp] += dp[i - 1][v][1]
                        dp[i][v][cmp] += preSum[200][2] - preSum[v][2]
                    else:
                        dp[i][v][cmp] += dp[i - 1][v][1]
                        dp[i][v][cmp] += preSum[200][2] - preSum[v][2]
            for v in range(1, 201):
                for cmp in range(3):
                    preSum[v][cmp] = preSum[v - 1][cmp] + dp[i][v][cmp]
        if arr[-1] != 0:
            return dp[N - 1][arr[-1]][2]
        else:
            res = 0
            for i in range(1, 201):
                res += dp[N - 1][i][2]
            return res


so = Solution()
arr = [6, 0, 9]
print(so.ways(arr))
print(so.waysDP(arr))
print(so.waysDP2(arr))