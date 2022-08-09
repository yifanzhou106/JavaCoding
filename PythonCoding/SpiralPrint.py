class Solution:

    def spiralPrint(self, nums):
        if not nums:
            raise Exception("error")
        self.rec(nums, 0, 0, 0)

    def rec(self, nums, i, j, dir):
        if i < len(nums) and j < len(nums[0]) and i >= 0 and j >= 0 and nums[i][j] != -1:
            print(nums[i][j])
            nums[i][j] = -1
        else:
            return
        if dir == 0:
            self.rec(nums, i, j + 1, dir)
            self.rec(nums, i + 1, j, dir)
            dir = 1
        if dir == 1:
            self.rec(nums, i, j - 1, dir)
            self.rec(nums, i - 1, j, dir)
            dir = 0


so = Solution()
arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15]]
so.spiralPrint(arr)