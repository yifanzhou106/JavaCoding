# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，
# 并将这些区域里所有的 'O' 用 'X' 填充。

# 不能一边遍历一边修改
# 需要优先把所有的数据都过一遍
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        can = [True]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    can[0] = True
                    self.process(board, i, j, can)
                    board[i][j] = 'T' if can[0] else 'F'

        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c == 'T' or c == 'F':
                    board[i][j] = '.'
                    self.change(board, i, j, c)

    def process(self, board, i, j, can):
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
            can[0] = False
            return
        if board[i][j] == 'O':
            board[i][j] = '.'
            self.process(board, i - 1, j, can)
            self.process(board, i + 1, j, can)
            self.process(board, i, j - 1, can)
            self.process(board, i, j + 1, can)

    def change(self, board, i, j, c):
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
            return

        if board[i][j] == '.':
            board[i][j] = 'X' if c == 'T' else 'O'
            self.change(board, i - 1, j, c)
            self.change(board, i + 1, j, c)
            self.change(board, i, j - 1, c)
            self.change(board, i, j + 1, c)

