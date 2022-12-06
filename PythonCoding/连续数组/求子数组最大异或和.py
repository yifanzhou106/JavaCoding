class TrieTree:
    def __init__(self):
        self.next = [None for _ in range(2)]


class NumTrie:
    def __init__(self):
        self.head = TrieTree()

    def insert(self, n):
        cur = self.head
        for i in range(31, -1, -1):
            path = (n >> i) & 1
            if not cur.next[path]:
                cur.next[path] = TrieTree()
            cur = cur.next[path]

    def findMax(self, n):
        cur = self.head
        res = int(0)
        if n < 0:
            res = -1 << 32
        for i in range(31, -1, -1):
            path = (n >> i) & 1
            best = path if i == 31 else (1 ^ path)
            if not cur.next[best]:
                best = 1 ^ best
            res = (path ^ best) << i | res
            cur = cur.next[best]
        return res


# n^3
class Solution:
    def findLargestXorSum1(self, nums):
        res = - float('inf')
        for i in range(len(nums)):
            for start in range(0, i):
                xor = 0
                for k in range(start, i):
                    xor = xor ^ nums[k]
                res = max(res, xor)
        return res

    # n^2
    def findLargestXorSum2(self, arr):
        if not arr:
            return 0
        xSum = 0
        res = - float('inf')
        for i in range(len(arr)):
            xSum = xSum ^ arr[i]
            temp = xSum
            for j in range(i):
                temp = temp ^ arr[j]
                res = max(res, temp)
        return res

    # n
    def findLargestXorSum3(self, arr):
        xSum = 0
        res = -float('inf')
        numTree = NumTrie()
        numTree.insert(0)
        for i in range(len(arr)):
            xSum = xSum ^ arr[i]
            temp = numTree.findMax(int(xSum))
            res = max(res, temp)
            numTree.insert(xSum)
        return res


so = Solution()
nums = [1, 2, 3, 5, -1, -7]
print(so.findLargestXorSum1(nums))
print(so.findLargestXorSum2(nums))
print(so.findLargestXorSum3(nums))

