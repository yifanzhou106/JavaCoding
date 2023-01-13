# 给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        isVisited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = self.process(board, isVisited, word, i,j,0)
                if res:
                    return True
        return False

    def process(self,board, isVisited, word, i,j,k):
        if k == len(word)-1:
            return board[i][j] == word[k]
        res = False
        if board[i][j] != word[k]:
            return res
        isVisited[i][j] = True
        if i > 0 and not isVisited[i-1][j]:
            res |= self.process(board, isVisited, word, i-1,j,k+1)
        if j > 0 and not isVisited[i][j-1]:
            res |= self.process(board, isVisited, word, i,j-1,k+1)
        if i < len(board)-1 and not isVisited[i+1][j]:
            res |= self.process(board, isVisited, word, i+1,j,k+1)
        if j < len(board[0]) -1 and not isVisited[i][j+1]:
            res |= self.process(board, isVisited, word, i,j+1,k+1)
        isVisited[i][j] = False
        return res
