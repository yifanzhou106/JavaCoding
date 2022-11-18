class Solution:
    def subArraySum2(self, arr, k):
        curSum = 0
        dir = {}
        dir[0] = -1
        res = -1

        for i in range(len(arr)):
            curSum += arr[i]
            if curSum - k in dir:
                left = dir[curSum - k]
                res = max(res, i - left)
            if curSum not in dir:
                dir[curSum] = i
        return res


so = Solution()
arr = [5, 6, 4, -3, 0, 3]
print(so.subArraySum2(arr, 10))
