# 请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
#
# 数字1-9在每一行只能出现一次。
# 数字1-9在每一列只能出现一次。
# 数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
#
# 注意：
#
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 空白格用'.'表示。

# 用三个矩阵，代表i行上，是否出现过数字，
# i列上，是否出现过数字，
# 第i个9宫格上，是否出现过数字
# 出现过就返回False
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row[2][3] 代表2行上，是否出现过3
        row = [[False for _ in range(10)] for _ in range(9)]
        # col[2][3] 代表2列上，是否出现过3
        col = [[False for _ in range(10)] for _ in range(9)]
        # box[2][3] 代表第二个9宫格上，是否出现过3
        box = [[False for _ in range(10)] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    bid = 3 * (i // 3) + j // 3
                    num = ord(board[i][j]) - ord('0')
                    if row[i][num] or col[j][num] or box[bid][num]:
                        return False
                    row[i][num] = True
                    col[j][num] = True
                    box[bid][num] = True
        return True