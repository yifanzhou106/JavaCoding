class Solution:
    def findLongestSubarraySumLessThanAim(self, arr, aim):
        if not arr:
            return 0
        min_sum = [None for _ in range(len(arr))]
        min_index = [None for _ in range(len(arr))]
        min_sum[-1] = arr[-1]
        min_index[-1] = len(arr) - 1
        for i in range(len(arr) - 2, -1, -1):
            if min_sum[i + 1] > 0:
                min_sum[i] = arr[i]
                min_index[i] = i
            else:
                min_sum[i] = arr[i] + min_sum[i + 1]
                min_index[i] = min_index[i + 1]
        print(min_sum)
        print(min_index)

        res = 0
        r = 0
        _sum = 0
        for i in range(len(arr)):
            while r < len(arr) and (_sum + min_sum[r]) <= aim:
                _sum += min_sum[r]
                r = min_index[r] + 1
            _sum -= arr[i] if r > i else 0
            res = max(res, r - i)
            r = max(r, i + 1)
        return res


so = Solution()
arr = [1, -3, 4, -5, 7, 3, -6, 9]
print(so.findLongestSubarraySumLessThanAim(arr, 1))