# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        return self.process(nums, 0, len(nums) - 1)

    def process(self, nums, left, right):
        if left == right:
            return TreeNode(nums[left])
        if left > right:
            return

        mid = left + ((right - left) >> 1)
        node = TreeNode(nums[mid])
        node.left = self.process(nums, left, mid - 1)
        node.right = self.process(nums, mid + 1, right)
        return node