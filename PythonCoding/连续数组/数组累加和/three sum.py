class Solution:
    def twoSum(self, arr, start, target, f):
        left = start
        right = len(arr) - 1
        res = []
        while left <= right:
            _sum = arr[left] + arr[right]
            if _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
            else:
                if left == 0 or arr[left] != arr[left - 1]:
                    res.append([f, arr[left], arr[right]])
                left += 1
        return res

    def threeSum(self, arr, target):
        arr.sort()
        res = []

        for i in range(len(arr)):
            t = target - arr[i]
            if i > 0 and arr[i - 1] == arr[i]:
                continue
            res += self.twoSum(arr, i + 1, t, arr[i])
        return res


so = Solution()
arr = [3, 2, 7, 6, 3, 1, 1, 9, 3, 4]
print(so.threeSum(arr, 10))