class Solution:
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
