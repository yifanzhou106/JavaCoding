class Solution:
    # 返回值
    def twoSum1(self, arr, target):
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

    # 返回index
    def twoSum2(self, arr, t):
        map = {}
        res = []
        for i in range(len(arr)):
            if t - arr[i] in map:
                print(t - arr[i], arr[i])
                res.append([map[t - arr[i]], i])
            map[arr[i]] = i
        return res


so = Solution()
arr = [3, 2, 7, 6, 3, 1, 1, 9, 3, 4]
print(so.twoSum1(arr, 10))
arr = [3, 2, 7, 6, 3, 1, 9, 3, 4]
print(so.twoSum2(arr, 10))
