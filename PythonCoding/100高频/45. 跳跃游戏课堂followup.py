# 跳棋，给定初始位置start， 结束位置end
# arr上每个值代表了在当前i位置只能向左或向右正好arr[i]步
# 求最少步数，没有就返回-1

# 使用宽度优先遍历, level map 记录level
# 最早找到end的就是最优解
class Solution:
    def jumpGameFollowUp(self, arr, start, end):
        q = [start]
        levelMap = [None for _ in range(len(arr))]
        levelMap[start] = 0

        while q:
            cur = q.pop(0)
            level = levelMap[cur]
            if cur == end:
                return level
            else:
                left = cur - arr[cur]
                right = cur + arr[cur]
                if left >= 0 and not levelMap[left]:
                    q.append(left)
                    levelMap[left] = level + 1
                if right < len(arr) and not levelMap[right]:
                    q.append(right)
                    levelMap[right] = level + 1
        return -1


so = Solution()
arr = [7, 2, 1, 3, 1, 4, 2, 1]
print(so.jumpGameFollowUp(arr, 3, 7))