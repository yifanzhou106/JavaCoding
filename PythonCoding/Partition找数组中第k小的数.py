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