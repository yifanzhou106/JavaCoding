#  数组从头跳到最后的最小步数
class Solution:
    def minStepToEnd(self, arr):
        if not arr:
            return 0
        return self.process(arr, 0)

    def process(self, arr, start):
        if start == len(arr) - 1:
            return 0
        if arr[start] >= len(arr) - start:
            return 1
        res = float('inf')
        for step in range(1, arr[start] + 1):
            res = min(res, 1 + self.process(arr, start + step))

        return res

    def minStepToEndDP(self, arr):
        if not arr:
            return 0
        dp = [float('inf') for _ in range(len(arr))]
        dp[-1] = 0
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] >= len(arr) - i:
                dp[i] = 1
            else:
                for j in range(1, arr[i] + 1):
                    if i + j < len(arr):
                        dp[i] = min(dp[i], 1 + dp[i + j])
        return dp[0]

    def minStepToEndDP2(self, arr):
        step = 0
        curR = 0
        next = -1
        for i in range(len(arr)):
            if i > curR:
                step += 1
                curR = next
                next = -1
            next = max(next, i + arr[i])
        return step


so = Solution()
arr = [3, 1, 6, 1, 2, 1, 2, 2, 3]

print(so.minStepToEnd(arr))
print(so.minStepToEndDP(arr))
print(so.minStepToEndDP2(arr))

arr = [3, 2, 3, 1, 1, 4]

print(so.minStepToEnd(arr))
print(so.minStepToEndDP(arr))
print(so.minStepToEndDP2(arr))
