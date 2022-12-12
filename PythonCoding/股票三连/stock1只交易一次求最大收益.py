class Solution:

    def stock1(self, arr):
        minVal = arr[0]
        res = 0
        for i in range(len(arr)):
            res = max(res, arr[i] - minVal)
            minVal = min(minVal, arr[i])
        return res


so = Solution()
n = [2, 5, 3, 2, 6, 4, 3]

print(so.stock1(n))