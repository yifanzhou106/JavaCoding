class TrieTree:
    def __init__(self):
        self.next = [None for _ in range(2)]


class NumTrie:
    def __init__(self):
        self.head = TrieTree()

    def add(self, xor):
        cur = self.head
        for i in range(31, -1, -1):
            path = (xor >> i) & 1
            if not cur.next[path]:
                cur.next[path] = TrieTree()
            cur = cur.next[path]

    def findMax(self, xor):
        cur = self.head
        res = 0
        for i in range(31, -1, -1):
            path = xor >> i & 1
            best = path if i == 31 else path ^ 1
            best = best if cur.next[best] else best ^ 1
            res = best << i | res
            cur = cur.next[best]
        return res


class Solution:
    def findLargestXorSum(self, nums):
        res = 0
        for i in range(len(nums)):
            for start in range(0, i):
                xor = 0
                for k in range(start, i):
                    xor = xor ^ nums[start]
                res = max(res, xor)
        return res

    def findLargestXorSumUsingTrieTree(self, nums):
        if not nums:
            return 0
        xor = 0
        res = -float('inf')
        numTree = NumTrie()
        numTree.add(0)
        for num in nums:
            xor = xor ^ num
            res = max(res, numTree.findMax(xor))
            numTree.add(xor)
        return res


so = Solution()

nums = [1, 2, 3, 5, -1, -7]
print(so.findLargestXorSum(nums))
print(so.findLargestXorSumUsingTrieTree(nums))