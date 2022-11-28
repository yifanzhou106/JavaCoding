class Solution:
    def findMaxAbsAnswerLeftMaxMinusRightMax(self, arr):
        if not arr:
            return 0
        rightMax = [None for _ in range(len(arr))]
        rightMax[-1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            rightMax[i] = max(arr[i], rightMax[i + 1])

        leftMax = arr[0]
        ans = 0
        for i in range(len(arr) - 1):
            ans = max(ans, abs(leftMax - rightMax[i + 1]))
            leftMax = max(leftMax, arr[i + 1])
        return ans

# 数组中的最大值，两头的数总是在另一边，且限制了其最小值，所以数组最大数-两侧头的最小值，就是答案
    def findMaxAbsAnswerLeftMaxMinusRightMax2(self, arr):
        if not arr:
            return 0
        maxNum = max(arr)
        lessVal = arr[0] if arr[0] < arr[-1] else arr[-1]
        return maxNum - lessVal


so = Solution()
arr = [3, 2, 7, 6, 3, 1, 9, 3, 4]
print(so.findMaxAbsAnswerLeftMaxMinusRightMax(arr))