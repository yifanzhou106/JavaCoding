class Solution:
    def findResult(self, arr):
        res = -float('inf')
        sums = [0 for _ in range(len(arr) + 1)]
        for i in range(len(arr)):
            sums[i + 1] = sums[i] + arr[i]
        print(sums)
        closestSmaller = self.findClosestSmallerNumAround(arr)
        print(closestSmaller)

        for i in range(len(arr)):
            left = closestSmaller[i][0]
            right = closestSmaller[i][0]
            res = max(res, self.findRangeSum(sums, left, right) * arr[i])
        return res

    def findClosestSmallerNumAround(self, arr):
        stack = []
        res = [[-1 for _ in range(2)] for _ in range(len(arr))]
        for i in range(len(arr)):
            while stack and arr[stack[-1][0]] > arr[i]:
                indexList = stack.pop()
                leftSmaller = -1 if not stack else stack[-1][-1]
                for i in indexList:
                    res[i][0] = leftSmaller
                    res[i][1] = arr[i]

            if stack and arr[stack[-1][0]] == arr[i]:
                stack[-1].append(i)
            else:
                stack.append([i])
        while stack:
            indexList = stack.pop()
            leftSmaller = -1 if not stack else stack[-1][-1]
            for i in indexList:
                res[i][0] = leftSmaller
                res[i][1] = len(arr)

    def findRangeSum(self, sums, L, R):
        return sums[R] - sums[L + 1]