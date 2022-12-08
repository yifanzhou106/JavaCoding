class Solution:
    def findMinSubarrySortedNeeded(self, arr):
        if not arr:
            return
        leftMax = arr[0]
        r = -1
        for i in range(1, len(arr)):
            if leftMax > arr[i]:
                r = i
            leftMax = max(leftMax, arr[i])
        rightMin = arr[-1]
        l = -1
        for i in range(len(arr) - 2, -1, -1):
            if rightMin < arr[i]:
                l = i
            rightMin = min(rightMin, arr[i])
        return [l, r]


so = Solution()
arr = [1, 2, 5, 3, 2, 4, 6, 7]
print(so.findMinSubarrySortedNeeded(arr))
