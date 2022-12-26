# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


class Solution:
    def mergeSort(self, arr):
        self.res = []
        if len(arr) > 1:
            self.rec(arr, 0, len(arr) - 1)
        return self.res

    def rec(self, arr, l, r):
        print(l, r)
        if l == r:
            return []
        mid = l + ((r - l) >> 1)
        self.rec(arr, l, mid)
        self.rec(arr, mid + 1, r)
        self.merge(arr, l, r, mid)

    def merge(self, arr, l, r, mid):
        help = []
        p1 = l
        p2 = mid + 1

        while p1 <= mid and p2 <= r:
            if arr[p1] <= arr[p2]:
                help.append(arr[p1])
                p1 += 1
            else:
                k = p1
                while k <= mid:
                    temp = []
                    temp.append(arr[k])
                    temp.append(arr[p2])
                    self.res.append(temp)
                    k += 1
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


so = Solution()
arr = [1, 3, 4, 2, 5, 1]
print(so.mergeSort(arr))