# 总体思路：
# 先算出开头长为k的sum和的数组即为rangeSum
# 从左向右得到到达i位置，最大sum的左边界，即为left
# 从右向左得到到达i位置，最大sum的左边界，即为right
# 中间的部分从k开始移动到n-2k+1之间，比较左侧最大值+中间+右侧的和
class Solution:
    # 记录左右边最大子数组和时的位置
    def subArrayMaxSum2(self, arr, k):
        # 记录从i开始的长度为k的子数组和,不在记录最大
        rangeSum = [0 for _ in range(len(arr))]
        # 记录从左向右的最大子数组和的左边界
        left = [0 for _ in range(len(arr))]
        _sum = 0
        for i in range(k):
            _sum += arr[i]
        _max = _sum
        rangeSum[0] = _sum
        # i代表新加入的位置，窗口的尾巴
        for i in range(k, len(arr)):
            _sum = _sum - arr[i - k] + arr[i]
            rangeSum[i - k + 1] = _sum
            left[i] = left[i - 1]
            if _sum > _max:
                _max = _sum
                left[i] = i - k + 1
        print(rangeSum, left)
        _sum = 0
        # 记录从右向左的最大子数组和的左边界
        right = [0 for _ in range(len(arr))]
        for i in range(len(arr) - 1, len(arr) - k - 1, -1):
            _sum += arr[i]
        _max = _sum
        # 记录左边界
        right[len(arr) - k] = len(arr) - k
        for i in range(len(arr) - k - 1, -1, -1):
            _sum = _sum - arr[i + k] + arr[i]
            right[i] = right[i + 1]
            if _sum > _max:
                _max = _sum
                right[i] = i
        print(right)
        # i 是中间部分的开头
        _max = -float('inf')
        a = 0
        b = 0
        c = 0
        for i in range(k, len(arr) - 2 * k + 1):
            # 当k到达i位置时，i-1位置上的最大子数组和的左边界是left[i-1]
            p1 = rangeSum[left[i - 1]]
            p2 = rangeSum[i]
            # 当k到达i位置时，i+k位置上的最大子数组和的左边界是right[i+k]
            p3 = rangeSum[right[i + k]]
            if p1 + p2 + p3 > _max:
                _max = p1 + p2 + p3
                a = left[i - 1]
                b = i
                c = right[i + k]
        print(_max)
        return [a, b, c]


so = Solution()
arr = [3, 1, -4, 6, 2, -8, 12, 4, 8, -9]

print(so.subArrayMaxSum2(arr, 3))

