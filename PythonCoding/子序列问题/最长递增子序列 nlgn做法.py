class Solution:
    def longestIncreasingSubsequence(self, arr):
        dp = [1 for _ in range(len(arr))]
        end = [arr[0]]
        res = 1
        for i in range(1, len(arr)):
            dp[i] = self.findLongestBeforeK(end, arr[i])
            res = max(res, dp[i])
        return res

    def findLongestBeforeK(self, end, k):
        if end[-1] < k:
            end.append(k)
            return len(end)
        return self.findClosestLarge(end, 0, len(end) - 1, k)

    def findClosestLarge(self, end, left, right, k):

        if left >= right:
            end[left] = k
            return left + 1
        mid = left + ((right - left) >> 1)
        if end[mid] > k:
            return self.findClosestLarge(end, left, mid - 1, k)
        else:
            return self.findClosestLarge(end, mid + 1, right, k)


so = Solution()
arr = [1, 2, 4, 8, 9, 5, 10, 3, 6, 7, 11]
inorder = [8, 4, 9, 2, 10, 5, 1, 6, 3, 11, 7]
print(so.longestIncreasingSubsequence(arr))


class Solution:
    def longestIncreasingSubsequence(self, arr):
        dp = [1 for _ in range(len(arr))]
        end = [None for _ in range(len(arr))]
        res = 1
        end[0] = arr[0]

        right = 0
        l = 0
        r = 0
        m = 0
        for i in range(1, len(arr)):
            l = 0
            r = right
            while l <= r:
                m = l + ((r - l) >> 1)
                if arr[i] > end[m]:
                    l = m + 1
                else:
                    r = m - 1
            end[l] = arr[i]
            right = max(right, l)
            dp[i] = l + 1
            res = max(res, dp[i])
        return res


so = Solution()
arr = [1, 2, 4, 8, 9, 5, 10, 3, 6, 7, 11]
inorder = [8, 4, 9, 2, 10, 5, 1, 6, 3, 11, 7]
print(so.longestIncreasingSubsequence(arr))