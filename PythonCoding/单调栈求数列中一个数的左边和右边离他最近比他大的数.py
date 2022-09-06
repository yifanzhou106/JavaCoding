class StackItem:
    def __init__(self, index, val):
        self.index = [index]
        self.val = val

    def add(self, index):
        self.index.append(index)


class Solution:

    def findFirstLargerNumLeftRight(self, nums):
        if not nums:
            return []
        stack = []
        larger = [[None for _ in range(len(nums))] for _ in range(2)]

        for i in range(len(nums)):
            if not stack:
                stack.append(StackItem(i, nums[i]))
                continue
            if nums[i] < stack[-1].val:
                stack.append(StackItem(i, nums[i]))
            elif nums[i] == stack[-1].val:
                stack[-1].index.append(i)
            else:
                while stack and nums[i] > stack[-1].val:
                    item = stack.pop()
                    for j in item.index:
                        larger[0][j] = None if not stack else stack[-1].val
                        larger[1][j] = nums[i]
                stack.append(StackItem(i, nums[i]))

        while stack:
            item = stack.pop()
            for j in item.index:
                larger[0][j] = None if not stack else stack[-1].val
                larger[1][j] = None
        return larger


so = Solution()
arr = [4, 6, 8, 12, 3, 4, 5]

print(so.findFirstLargerNumLeftRight(arr))

