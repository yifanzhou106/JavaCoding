class Solution:
    # 打气球，每次打一个气球得到分数,左侧最近没爆得气球（L）* 当前气球分（cur）*右侧最近没爆得气球（R）
    # 如果左边没有气球了 cur * R
    # 如果右边没有气球了 cur * L
    # 如果左右都没气球 cur
    def shotBalloon(self, arr):
        newArr = [1 for _ in range(len(arr) + 2)]
        for i in range(len(arr)):
            newArr[i + 1] = arr[i]

        return self.process(newArr, 1, len(arr))

    # 在LR范围中打爆气球的最高分，L-1,R+1的气球都没有爆
    # 看哪个气球是最后打爆的
    def process(self, arr, L, R):
        if L == R:
            return arr[L - 1] * arr[L] * arr[R + 1]
        # L是最后爆得
        p1 = arr[L - 1] * arr[L] * arr[R + 1] + self.process(arr, L + 1, R)
        # R是最后爆得
        p2 = arr[L - 1] * arr[R] * arr[R + 1] + self.process(arr, L, R - 1)

        res = max(p1, p2)
        for i in range(L + 1, R):
            res = max(res, arr[L - 1] * arr[i] * arr[R + 1] + self.process(arr, L, i - 1),
                      + self.process(arr, i + 1, R))
        return res


so = Solution()
arr = [3, 2, 5]
print(so.shotBalloon(arr))