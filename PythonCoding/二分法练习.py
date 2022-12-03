class Solution:
    def playground(self, arr, k):

        # 比k大等于的第一个数的位置
        l = 0
        r = len(arr) - 1
        m = 0
        while l <= r:
            m = l + ((r - l) >> 1)
            if arr[m] >= k:
                r = m - 1
            else:
                l = m + 1
        print(l)

        # 比k小等于的第一个数的位置
        l = 0
        r = len(arr) - 1
        m = 0
        ans = -1
        while l <= r:
            m = l + ((r - l) >> 1)
            if arr[m] > k:
                r = m - 1
            else:
                ans = m
                l = m + 1
        print(ans)


so = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14]
so.playground(arr, 9)