# o（n）最优解，先求出从右向左的最小累加和，代表i位之后的最小sum以及index表
# 从左往右使用双指针依次假如最小sum使其小于k，如果超了就左边缩
class Solution:
    def subArraySum3(self, arr, k):
        minSum = [0 for _ in range(len(arr))]
        minSumIndex = [0 for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                minSum[i] = arr[i]
                minSumIndex[i] = i
            else:
                if minSum[i + 1] <= 0:
                    minSum[i] = minSum[i + 1] + arr[i]
                    minSumIndex[i] = minSumIndex[i + 1]
                else:
                    minSum[i] = arr[i]
                    minSumIndex[i] = i
        print(minSum, minSumIndex)
        right = minSumIndex[0]
        curSum = 0
        res = -1

        for i in range(len(arr)):
            while right < len(arr) and curSum + minSum[right] <= k:
                curSum += minSum[right]
                right = minSumIndex[right] + 1
            res = max(res, right - i)
            if right > i:
                curSum -= arr[i]
            else:
                right = i + 1
        return res


so = Solution()
arr = [3, 7, 4, -6, 6, 3, -2, 0, 7, -3, 2]
print(so.subArraySum3(arr, 10))
