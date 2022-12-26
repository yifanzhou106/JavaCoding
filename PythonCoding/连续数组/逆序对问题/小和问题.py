# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


class Solution:
    def mergeSort(self, arr):
        if len(arr) > 1:
            return self.rec(arr, 0, len(arr) - 1)
        return 0

    def rec(self, arr, l, r):
        print(l, r)
        if l == r:
            return 0
        mid = l + ((r - l) >> 1)

        return self.rec(arr, l, mid) + self.rec(arr, mid + 1, r) + self.merge(arr, l, r, mid)

    def merge(self, arr, l, r, mid):
        help = []
        p1 = l
        p2 = mid + 1
        _sum = 0
        while p1 <= mid and p2 <= r:
            if arr[p1] < arr[p2]:
                _sum += arr[p1] * (r - p2 + 1)
                help.append(arr[p1])
                p1 += 1
            else:
                help.append(arr[p2])
                p2 += 1
        while p1 <= mid:
            help.append(arr[p1])
            p1 += 1
        while p2 <= r:
            help.append(arr[p2])
            p2 += 1
        for i in range(len(help)):
            arr[l] = help[i]
            l += 1
        print(help)
        return _sum


so = Solution()
arr = [1, 3, 4, 2, 5]
print(so.mergeSort(arr))