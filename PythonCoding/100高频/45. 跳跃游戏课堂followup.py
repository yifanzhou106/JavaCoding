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

    # 用dp来做， 假设最大步数小于arr长度-1
    # 因为假设要从start到end，最少距离的话，不会走重复的点
    # 所以从start到end最大的步数是arr长度-2
    def jumpGameFollowUp2(self, arr, start, end):
        return self.process(arr, end, start, 0)

    def process(self, arr, end, cur, k):
        if cur < 0:
            return -1
        if cur >= len(arr):
            return -1
        if k >= len(arr) - 1:
            return -1
        if cur == end:
            return k
        left = cur - arr[cur]
        right = cur + arr[cur]

        p1 = self.process(arr, end, left, k + 1)
        p2 = self.process(arr, end, right, k + 1)

        ans = -1
        if p1 != -1 and p2 != -1:
            ans = min(p1, p2)
        elif p1 != -1:
            ans = p1
        elif p2 != -1:
            ans = p2
        return ans


so = Solution()
arr = [7, 2, 1, 3, 1, 4, 2, 1]
print(so.jumpGameFollowUp(arr, 3, 7))
print(so.jumpGameFollowUp2(arr, 3, 7))