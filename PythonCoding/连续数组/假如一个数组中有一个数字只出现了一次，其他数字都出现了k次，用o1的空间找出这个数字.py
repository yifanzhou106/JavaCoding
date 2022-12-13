# 假如一个数组中有一个数字只出现了一次，其他数字都出现了k次，用o1的空间找出这个数字

class Solution:
    def findSingleNumber(self, arr, k):
        nums = [0 for _ in range(32)]
        for n in arr:
            self.tenToK(nums, n, k)
        print(nums)
        return self.kToTen(nums, k)

    def tenToK(self, nums, n, k):
        for i in range(32):
            nums[i] += n % k
            n //= k
            nums[i] %= k

    def kToTen(self, nums, k):
        res = 0
        temp = 1
        for i in range(32):
            res += nums[i] * temp
            temp *= k
        return res


so = Solution()
arr = [-1, -1, -1, -1, -1, 2, 2, 2, 4, 2, 2]
print(so.findSingleNumber(arr, 5))

arr = [1, 1, 1, 2, 6, 6, 2, 2, 10, 10, 10, 12, 12, 12, 6, 9]
print(so.findSingleNumber(arr, 3))