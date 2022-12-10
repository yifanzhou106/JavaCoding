#必须包含1

class Solution:
    def unformedSum3(self, arr):
        arr = sorted(arr)
        r = 1
        print(arr, len(arr))
        for i in range(1, len(arr)):
            if arr[i] > r + 1:
                return r + 1
            else:
                r += arr[i]
        return r + 1


so = Solution()
arr = [1, 2, 5, 3, 2, 4, 6, 7]
print(so.unformedSum3(arr))