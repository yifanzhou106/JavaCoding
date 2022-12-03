class Solution:
    def largestSubmetric(self, M):
        res = -float('inf')
        for i in range(len(M)):
            arr = []
            for j in range(i, len(M)):
                if not arr:
                    arr = M[i][:]
                else:
                    for k in range(len(arr)):
                        arr[k] += M[j][k]
                largest = self.largestSubarrSum(arr)
                print(arr, largest)

                res = max(res, largest)
        return res

    def largestSubarrSum(self, arr):
        dp = [None for _ in range(len(arr))]
        dp[0] = arr[0]
        res = arr[0]
        for i in range(1, len(arr)):
            dp[i] = dp[i - 1] + arr[i] if dp[i - 1] > 0 else arr[i]
            res = max(res, dp[i])
        return res


so = Solution()
M = [[-3, 5, 3, 1, -4], [6, -2, -1, 0, 7], [-9, 8, 3, 2, -111]]
print(so.largestSubmetric(M))