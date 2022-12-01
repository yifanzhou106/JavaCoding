import random


class Solution:
    def findNthSmallestCombinationOfTwoNum(self, arr, k):
        n = len(arr)
        if k > n * n:
            return []
        p1 = (k - 1) // n
        f = self.findKMin(arr, p1)
        less = 0
        count = 0
        for num in arr:
            if num < f:
                less += 1
            if num == f:
                count += 1
        p2 = k - (less * n)

        p2 = (p2 - 1) // count
        s = self.findKMin(arr, p2)
        return [f, s]

    def findKMin(self, arr, p):
        l = 0
        r = len(arr) - 1
        range = []
        while l < r:
            rand = random.randint(l, r)
            range = self.patition(arr, rand, l, r)
            if p < range[0]:
                r = range[0] - 1
            elif p > range[1]:
                l = range[1] + 1
            else:
                return arr[p]
        return arr[l]

    def patition(self, arr, k, l, r):
        left = l - 1
        right = r + 1
        m = arr[k]
        i = l
        while left < right and i < right:
            if arr[i] < m:
                left += 1
                arr[i], arr[left] = arr[left], arr[i]
                i += 1
            elif arr[i] > m:
                right -= 1
                arr[i], arr[right] = arr[right], arr[i]
            else:
                i += 1
        return [left + 1, right - 1]


so = Solution()
# arr = [3,2,7,6,3,1,1,9,3,4]
arr = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]
print(so.findNthSmallestCombinationOfTwoNum(arr, 46))