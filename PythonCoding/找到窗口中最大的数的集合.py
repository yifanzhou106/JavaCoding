class Node:
    def __init__(self, val=0, index=0):
        self.val = val
        self.index = index


class Solution:
    def findLargetNumsInWindow(self, nums, w):
        if not nums or w <= 0:
            return []
        res = []
        right = 0
        root = []

        while right < len(nums):
            if right < w:
                self.addNum(root, nums[right], right)
                right += 1
                if right == w:
                    res.append(root[0].val)
            else:
                self.removeNums(root, right, w)
                self.addNum(root, nums[right], right)
                res.append(root[0].val)
                right += 1
        return res

    def addNum(self, arr, val, index):
        while arr and arr[-1] and arr[-1].val <= val:
            arr.pop()
        arr.append(Node(val, index))

    def removeNums(self, arr, right, w):
        while arr and arr[0].index <= right - w:
            arr.pop(0)


so = Solution()
arr = [4, 6, 8, 2, 3, 4, 5, 6, 12, 3, 77, 34]
print(so.findLargetNumsInWindow(arr, 4))