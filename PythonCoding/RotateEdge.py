# Online Python compiler (interpreter) to run Python online.
class Solution:
    def rotateEdge(self, nums):
        if len(nums) != len(nums[0]):
            raise Exception("error")
        li, lj = 0, 0
        ri, rj = len(nums) - 1, len(nums[0]) - 1

        while li < ri:
            self.rotate(li, lj, ri, rj, nums)
            li += 1
            lj += 1
            ri -= 1
            rj -= 1

    def rotate(self, li, lj, ri, rj, nums):
        times = ri - li
        for i in range(times):
            temp = nums[li][lj + i]
            nums[li][lj + i] = nums[ri - i][lj]
            nums[ri - i][lj] = nums[ri][rj - i]
            nums[ri][rj - i] = nums[li + i][rj]
            nums[li + i][rj] = temp


so = Solution()
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
so.rotateEdge(arr)
print(arr)
