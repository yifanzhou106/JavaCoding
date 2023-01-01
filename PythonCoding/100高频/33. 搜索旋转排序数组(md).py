# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
# 例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为[4,5,6,7,0,1,2] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回-1。
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

# 直接二分法
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.process(nums, target, 0, len(nums)-1)


    def process(self, nums, t, left, right):
        if left == right:
            return left if nums[left] == t else -1
        if left > right:
            return -1

        mid = left + ((right - left) >> 1)
        if nums[mid] == t:
            return mid
        if nums[left] == t:
            return left
        if nums[right] == t:
            return right

        # [4,5,6,7,0,1,2]如果左边比中间小，那么左边的区间一定是递增的
        if nums[mid] >= nums[left]:
            if nums[left] < t < nums[mid]:
                return self.process(nums, t, left, mid - 1)
            else:
                return self.process(nums, t, mid + 1, right)
        # [4,5,6,0,1,2,3]不然右边的区间一定的递增的
        else:
            if nums[mid] < t < nums[right]:
                return self.process(nums, t, mid + 1, right)
            else:
                return self.process(nums, t, left, mid - 1)


