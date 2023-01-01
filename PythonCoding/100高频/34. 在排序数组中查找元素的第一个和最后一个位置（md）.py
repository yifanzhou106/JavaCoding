# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。
# 请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回[-1, -1]。
# 你必须设计并实现时间复杂度为O(log n)的算法解决此问题。
# 示例 1：
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]

# 二分法先确认target在数组内
# 再找target-0.5, target +0.5的位置
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        index = self.process(nums, target, 0, len(nums) - 1)
        if index >= len(nums) or index < 0 or nums[index] != target:
            return [-1, -1]
        return [self.process(nums, target - 0.5, 0, len(nums) - 1),
                max(0, self.process(nums, target + 0.5, 0, len(nums) - 1) - 1)]

    def process(self, nums, t, left, right):
        if left > right:
            return left

        mid = left + ((right - left) >> 1)

        if nums[mid] == t:
            return mid
        elif nums[mid] > t:
            return self.process(nums, t, left, mid - 1)
        else:
            return self.process(nums, t, mid + 1, right)

    # 方法2
    # 左边界mostLeft，用二分，每当nums[mid] >= t时，走左边更新mostLeft
    # 右边界mostRight，用二分，每当nums[mid] <= t时,走右边更新mostRight
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left = self.process1(nums, target)
        if nums[left] != target:
            return [-1, -1]
        right = self.process2(nums, target)
        return [left, right]

    def process1(self, nums, t):
        left = 0
        right = len(nums) - 1
        mostLeft = -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] >= t:
                mostLeft = mid
                right = mid - 1
            else:
                left = mid + 1
        return mostLeft

    def process2(self, nums, t):
        left = 0
        right = len(nums) - 1
        mostRight = -1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > t:
                right = mid - 1
            else:
                mostRight = mid
                left = mid + 1
        return mostRight

