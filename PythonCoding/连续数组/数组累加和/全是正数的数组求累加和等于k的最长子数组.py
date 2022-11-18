class Solution:

    def subArraySum(self, arr, k):
        if not arr:
            return 0
        left = 0
        right = 0
        winSum = arr[0]
        res = 0

        while right < len(arr):
            if winSum < k:
                right += 1
                if right == len(arr):
                    break
                winSum += arr[right]
            else:
                winSum -= arr[left]
                left += 1
            if winSum == k:
                res = max(res, right - left + 1)
        return res


so = Solution()
arr = [4, 3, 2, 6, 3, 2, 1, 1, 3, 2, 6]
print(so.subArraySum(arr, 6))
