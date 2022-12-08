import heapq


class Solution:
    def splitArrTo4PartsWithSameSum(self, arr):
        return self.process(arr, 3, 0, len(arr) - 1)

    def process(self, arr, rest, start, end):
        if rest == 0:
            return sum(arr[start:end + 1])
        if start == end:
            return arr[start]
        curSum = arr[start]
        for i in range(start + 1, end):
            right = self.process(arr, rest - 1, i + 1, end)
            if right and curSum == right:
                return curSum
            curSum += arr[i]
        return

# o(n), 通过map记录前缀和的位置，直接计算当前第一部分的和可不可能
    def splitArrTo4PartsWithSameSumBest(self, arr):
        map = {}
        cSum = 0
        for i in range(len(arr)):
            cSum += arr[i]
            map[cSum] = i
        print(map)
        cSum = arr[0]
        for i in range(1, len(arr)):
            splitSum = arr[i]
            j = 2
            tmpSum = cSum * j + splitSum
            while tmpSum in map:
                if j == 4:
                    return True
                next = map[tmpSum] + 1
                if next < len(arr):
                    j += 1
                    splitSum += arr[next]
                    tmpSum = cSum * j + splitSum
                else:
                    step = 0
                    break
            cSum += arr[i]
        return False


so = Solution()
nums = [3, 2, 4, 1, 4, 9, 5, 10, 1, 2, 2]
print(so.splitArrTo4PartsWithSameSum(nums))
print(so.splitArrTo4PartsWithSameSumBest(nums))
