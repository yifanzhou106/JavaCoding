class Solution:
    def twoSum(self, arr, target):
        arr.sort()
        left = 0
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
                    res.append([arr[left], arr[right]])
                left += 1
        return res


so = Solution()
arr = [3, 2, 7, 6, 3, 1, 1, 9, 3, 4]
print(so.twoSum(arr, 10))