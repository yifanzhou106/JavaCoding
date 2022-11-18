import random


class Solution:
    def findMinKth(self, nums, k):
        temp = nums[:]
        return self.rec(nums, 0, len(nums) - 1, k)

    def rec(self, nums, begin, end, target):
        if begin == end:
            return nums[begin]

        pivot = self.findRandomPivot(nums, begin, end)
        midRegion = self.partition(nums, begin, end, pivot)

        if target >= midRegion[0] and target <= midRegion[1]:
            return nums[target]
        elif target < midRegion[0]:
            return self.rec(nums, begin, midRegion[0] - 1, target)
        else:
            return self.rec(nums, midRegion[1] + 1, end, target)

    def findRandomPivot(self, nums, begin, end):
        rIndex = random.randint(begin, end)
        return nums[rIndex]

    def partition(self, nums, begin, end, pivot):
        less = begin - 1
        more = end + 1
        cur = begin

        while cur < more:
            if nums[cur] > pivot:
                nums[cur], nums[more - 1] = nums[more - 1], nums[cur]
                more -= 1
            elif nums[cur] < pivot:
                nums[cur], nums[less + 1] = nums[less + 1], nums[cur]
                less += 1
                cur += 1
            else:
                cur += 1
        return [less + 1, more - 1]


so = Solution()
arr = [4, 6, 8, 2, 3, 4, 5, 6, 123, 3, 77, 34]
print(so.findMinKth(arr, 6))

# 2刷
import random


class Solution:

    def findKSmallestNumber(self, nums, k):
        if len(nums) < k:
            return nums[-1]
        return self.process(nums, 0, len(nums) - 1, k)

    def process(self, nums, left, right, k):
        if left == right:
            return nums[left]

        randIndex = random.randint(left, right)
        equalRange = self.patition(nums, left, right, nums[randIndex])

        if k >= equalRange[0] and k <= equalRange[1]:
            return nums[k]
        elif k < equalRange[0]:
            return self.process(nums, left, equalRange[0] - 1, k)
        else:
            return self.process(nums, equalRange[1] + 1, right, k)

    def patition(self, nums, left, right, m):
        l = left - 1
        r = right + 1
        cur = left

        while cur < r:
            if nums[cur] < m:
                nums[l + 1], nums[cur] = nums[cur], nums[l + 1]
                l += 1
                cur += 1
            elif nums[cur] == m:
                cur += 1
            else:
                nums[r - 1], nums[cur] = nums[cur], nums[r - 1]
                r -= 1
        return [l + 1, r - 1]


so = Solution()
nums = [5, 9, 8, 2, 1, 4, 6, 2, 7]
print(so.findKSmallestNumber(nums, 3))

