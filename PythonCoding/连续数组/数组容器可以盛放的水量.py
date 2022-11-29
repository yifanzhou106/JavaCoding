# 用从右向左的最大值辅助数组解，每个节点的值都应该是max（min（左侧最大值右侧最大值）-arr[i], 0）
class Solution:
    def findVolumn(self, arr):
        if not arr or len(arr) < 3:
            return 0
        rightMax = [None for _ in range(len(arr))]
        rightMax[-1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            rightMax[i] = max(arr[i], rightMax[i + 1])
        res = 0
        leftMax = arr[0]
        for i in range(1, len(arr)):
            level = min(rightMax[i], leftMax)
            if level > arr[i]:
                res += (level - arr[i])
            leftMax = max(leftMax, arr[i])
        return res

# 用双指针优化
    def findVolumn2(self, arr):
        if not arr or len(arr) < 3:
            return 0
        rightMax = arr[-1]
        leftMax = arr[0]
        left = 1
        right = len(arr) - 2
        res = 0
        while left <= right:
            if leftMax < rightMax:
                res += max(leftMax - arr[left], 0)
                leftMax = max(leftMax, arr[left])
                left += 1
            else:
                res += max(rightMax - arr[right], 0)
                rightMax = max(rightMax, arr[right])
                right -= 1
        return res


so = Solution()
arr = [3, 1, 2, 5, 2, 4]
print(so.findVolumn2(arr))
