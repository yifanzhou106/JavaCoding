class Solution:
    # 孩子分数为score arr，要求每个孩子至少一颗糖，相邻两个孩子分数大的要比分数小的糖多
    # 坡度问题，用辅助数组
    def candi1(self, score):
        left = [1 for _ in range(len(score))]
        right = [1 for _ in range(len(score))]
        res = [1 for _ in range(len(score))]
        # 计算出从左向右的坡度
        for i in range(1, len(score)):
            if score[i] > score[i - 1]:
                left[i] = left[i - 1] + 1
        # 计算出从右向左的坡度
        for i in range(len(score) - 2, -1, -1):
            if score[i] > score[i + 1]:
                right[i] = right[i + 1] + 1
        # 左右坡度的最大值就是答案
        for i in range(1, len(score)):
            res[i] = max(left[i], right[i])
        return res

    # 孩子分数为score arr，要求每个孩子至少一颗糖，相邻两个孩子分数大的要比分数小的糖多
    # 如果分数相等的话，糖数要一样
    def candi2(self, score):
        left = [1 for _ in range(len(score))]
        right = [1 for _ in range(len(score))]
        res = [1 for _ in range(len(score))]
        # 计算出从左向右的坡度
        for i in range(1, len(score)):
            if score[i] > score[i - 1]:
                left[i] = left[i - 1] + 1
            elif score[i] == score[i - 1]:
                left[i] = left[i - 1]
        # 计算出从右向左的坡度
        for i in range(len(score) - 2, -1, -1):
            if score[i] > score[i + 1]:
                right[i] = right[i + 1] + 1
            elif score[i] == score[i + 1]:
                right[i] = right[i + 1]
        # 左右坡度的最大值就是答案
        for i in range(1, len(score)):
            res[i] = max(left[i], right[i])
        return res


so = Solution()
arr = [1, 2, 3, 3, 1, 4, 4, 2]
print(so.candi1(arr))
arr = [1, 2, 2, 3, 3, 4, 4, 4, 4, 2, 1, -1, -2]
print(so.candi2(arr))