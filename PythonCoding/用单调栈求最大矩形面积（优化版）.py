class Item:
    def __init__(self, val=0, index=None):
        self.val = val
        self.index = [index]


class Solution:
    def largestSizeOfRectangle(self, mx):
        if not mx:
            return 0
        height = [0 for _ in range(len(mx[0]))]
        for i in range(len(mx)):
            for j in range(len(mx[0])):
                height[j] = 0 if mx[i][j] == 0 else height[j] + 1
        stack = []
        leftClosestMin = [None for _ in range(len(mx[0]))]
        rightClosestMin = [None for _ in range(len(mx[0]))]

        for i in range(len(height)):
            if not stack:
                stack.append(Item(height[i], i))
            elif stack[-1].val < height[i]:
                stack.append(Item(height[i], i))
            elif stack[-1].val == height[i]:
                stack[-1].index.append(i)
            else:
                while stack and stack[-1].val > height[i]:
                    item = stack.pop()
                    for j in item.index:
                        if not stack:
                            leftClosestMin[j] = None
                        else:
                            leftClosestMin[j] = stack[-1].index[-1]
                        rightClosestMin[j] = i
                stack.append(Item(height[i], i))
        while stack:
            item = stack.pop()
            for j in item.index:
                if not stack:
                    leftClosestMin[j] = None
                else:
                    leftClosestMin[j] = stack[-1].index[-1]
                rightClosestMin[j] = None
        res = -1
        print(leftClosestMin)
        print(rightClosestMin)
        for i in range(len(leftClosestMin)):
            leftMin = 0 if not leftClosestMin[i] else leftClosestMin[i] + 1
            rightMin = len(mx[0]) - 1 if not rightClosestMin[i] else rightClosestMin[i] - 1

            res = max(res, height[i] * (rightMin - leftMin + 1))
        return res


class Item:
    def __init__(self, val=0, index=None):
        self.val = val
        self.index = [index]


class Solution:
    def largestSizeOfRectangle(self, mx):
        if not mx:
            return 0
        res = 0
        height = [0 for _ in range(len(mx[0]))]
        for i in range(len(mx)):
            for j in range(len(mx[0])):
                height[j] = 0 if mx[i][j] == 0 else height[j] + 1
            res = max(res, self.findMaxRecSize(height))
        return res

    def findMaxRecSize(self, height):
        stack = []
        res = 0
        for i in range(len(height)):
            if not stack:
                stack.append(Item(height[i], i))
            elif stack[-1].val < height[i]:
                stack.append(Item(height[i], i))
            elif stack[-1].val == height[i]:
                stack[-1].index.append(i)
            else:
                while stack and stack[-1].val > height[i]:
                    item = stack.pop()
                    for j in item.index:
                        left = 0
                        if stack:
                            left = stack[-1].index[-1] + 1
                        right = i - 1
                        res = max(res, height[j] * (right - left + 1))
                stack.append(Item(height[i], i))
        while stack:
            item = stack.pop()
            for j in item.index:
                left = 0
                right = len(height) - 1
                if stack:
                    left = stack[-1].index[-1] + 1
                res = max(res, height[j] * (right - left + 1))
        return res


so = Solution()
arr = [[1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]
print(so.largestSizeOfRectangle(arr))

so = Solution()
arr = [[0, 0, 0, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
print(so.largestSizeOfRectangle(arr))

