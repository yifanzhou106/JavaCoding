# Python没有内置的treeset类，需要自己implement，或者用Java

class Solution:
    def subArraySumlessEqlk(self, arr, k):
        treeSet = TreeSet()
        treeSet.add(0)
        cur = 0
        res = -float('inf')
        for i in range(len(arr)):
            cur += arr[i]
            if treeset.ceiling(cur - k):
                res = max(res, cur - treeSet.ceiling(cur - k) )
            treeSet.add(cur)
        return res


so = Solution()
arr = [3, 7, 4, -6, 6, 3, -2, 0, 7, -3, 2]
print(so.subArraySum3(arr, 10))
