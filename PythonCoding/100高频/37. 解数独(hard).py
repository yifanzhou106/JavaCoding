# 编写一个程序，通过填充空格来解决数独问题。
#
# 数独的解法需 遵循如下规则：
#
# 数字1-9在每一行只能出现一次。
# 数字1-9在每一列只能出现一次。
# 数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用'.'表示。

# 用三个矩阵，代表i行上，是否出现过数字，
# i列上，是否出现过数字，
# 第i个9宫格上，是否出现过数字
# 出现过就返回False
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [[False for _ in range(10)] for _ in range(9)]
        col = [[False for _ in range(10)] for _ in range(9)]
        box = [[False for _ in range(10)] for _ in range(9)]
        # 先遍历一遍，把所有数字部分的辅助矩阵位置给填上TRUE
        self.init(board,row,col,box)
        self.process(board,row,col,box,0,0)
        return board

    def init(self,board,row,col,box ):
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    bid = 3 * (i // 3) + j // 3
                    num = ord(board[i][j]) - ord('0')
                    row[i][num] = True
                    col[j][num] = True
                    box[bid][num] = True

    def process(self, board, row, col, box, i, j):
        if i  == len(board) :
            return True
        nextJ = 0 if j == 8 else j + 1
        nextI = i + 1 if j == 8 else i
        bid = 3 * (i // 3) + j // 3
        if board[i][j] != '.':
            return self.process(board, row, col, box, nextI, nextJ)
        else:
            # 不是数字的部分尝试1-9里可以满足条件的
            for n in range(1,10):
                if not row[i][n] and not col[j][n] and not box[bid][n]:
                    board[i][j] = str(n)
                    row[i][n] = True
                    col[j][n] = True
                    box[bid][n] = True
                    if self.process(board, row, col, box, nextI, nextJ):
                        return True
                    board[i][j] = '.'
                    row[i][n] = False
                    col[j][n] = False
                    box[bid][n] = False
        return False



