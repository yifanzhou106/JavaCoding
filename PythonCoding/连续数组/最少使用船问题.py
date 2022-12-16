# 给定一个arr，代表人的体重，limit代表船的载重
# 船每次最多只能载两个人，且总体重数不能超过船的载重
# 求最少船的次数
# 排序后到limit/2处左右双指针移动
# 答案为 左右两边同时解决的数量+（左边没解决的数量+1）//2 + 右边没有解决的数量

class Solution:

    def minBoat(self, arr, limit):
        arr = sorted(arr)
        if arr[-1] > limit:
            return -1

        left = 0
        right = 0
        while arr[right] <= limit // 2:
            right += 1

        left = right - 1
        leftUnsolved = 0
        solved = 0
        while left >= 0 and right < len(arr):
            if arr[left] + arr[right] > limit:
                leftUnsolved += 1
                left -= 1
            else:
                solved += 1
                left -= 1
                right += 1
        return (left + 1 + leftUnsolved + 1) // 2 + solved + len(arr) - right

# 第二种做法
    def minBoat2(self, arr, limit):
        arr = sorted(arr)
        if arr[-1] > limit:
            return -1

        left = 0
        right = 0
        while arr[right] <= limit // 2:
            right += 1

        left = right - 1
        leftUnsolved = 0
        totalSolved = 0
        while left >= 0:
            solved = 0
            while right < len(arr) and arr[left] + arr[right] <= limit:
                right += 1
                solved += 1
            totalSolved += solved
            if solved == 0:
                leftUnsolved += 1
                left -= 1
            else:
                left = max(-1, left - solved)

        return (leftUnsolved + 1) // 2 + totalSolved + len(arr) - right


so = Solution()
arr = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9]
print(so.minBoat(arr, 10))
print(so.minBoat2(arr, 10))
