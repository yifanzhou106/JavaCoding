class Solution:
    def findSpotCoveredByLine(self, arr, k):
        if not arr or k == 0:
            return 0
        res = 0
        right = 0
        for i in range(len(arr)):
            while right < len(arr) and arr[right] - arr[i] <= k:
                res = max(res, right - i + 1)
                right += 1

        return res


so = Solution()
arr = [2, 6, 8, 10, 17, 19]
print(so.findSpotCoveredByLine(arr, 6))
