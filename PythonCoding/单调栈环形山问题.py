class Pair:
    def __init__(self, val=0, count=0):
        self.val = val
        self.count = count


class Solution:
    def findMountPair(self, nums):
        if not nums:
            return 0
        maxIndex = 0
        for i in range(len(nums)):
            maxIndex = i if nums[i] > nums[maxIndex] else maxIndex

        stack = [Pair(nums[maxIndex], 1)]
        next = self.findNext(nums, maxIndex)
        res = 0
        while next != maxIndex:
            while stack and stack[-1].val < nums[next]:
                pair = stack.pop()
                res += self.calculateCombination(pair.count) + pair.count
                res += 0 if not stack else pair.count
            if stack and stack[-1].val == nums[next]:
                stack[-1].count += 1
            else:
                stack.append(Pair(nums[next], 1))
            next = self.findNext(nums, next)
        while stack:
            pair = stack.pop()
            if len(stack) >= 2:
                res += self.calculateCombination(pair.count) + 2 * pair.count
            elif len(stack) == 1:
                res += self.calculateCombination(pair.count) + pair.count
                if stack[-1].count > 1:
                    res += pair.count
            else:
                res += self.calculateCombination(pair.count)
        return res

    def findNext(self, nums, i):
        return 0 if i == len(nums) - 1 else i + 1

    def calculateCombination(self, n):
        return 0 if n == 1 else n * (n - 1) // 2


so = Solution()
arr = [5, 5, 4, 4, 3, 3]
print(so.findMountPair(arr))

arr = [5, 5, 4, 4, 2, 1, 3, 3]
print(so.findMountPair(arr))

