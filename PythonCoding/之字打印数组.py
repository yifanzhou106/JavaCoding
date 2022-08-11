class Solution:
    def printMatrix(self, nums):
        self.res = []
        li, lj, ri, rj = 0, 0, 0, 0
        flag = False
        while (li != len(nums) and lj != len(nums[0])):
            self.printLine(nums, li, lj, ri, rj, flag)
            flag = not flag
            if lj + 1 < len(nums[0]):
                lj += 1
            else:
                li += 1
            if ri + 1 < len(nums):
                ri += 1
            else:
                rj += 1
        return self.res

    def printLine(self, nums, li, lj, ri, rj, flag):
        temp = []
        while li != ri and lj != rj:
            temp.append(nums[ri][rj])
            ri -= 1
            rj += 1
        temp.append(nums[li][lj])
        if flag:
            self.res.append(temp[::-1])
        else:
            self.res.append(temp[:])


so = Solution()
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print(so.printMatrix(arr))