# 用来比较地址
class Dot:
    def __init__(self):
        return


class UnionFind:
    def __init__(self, metrix):
        self.fatherMap = {}
        self.sizeMap = {}
        self.cellingSet = set()
        self.N = len(metrix)
        self.M = len(metrix[0])
        self.cellingAll = 0
        self.dots = [[None for _ in range(self.M)] for _ in range(self.N)]
        self.grid = metrix
        self.initAll()

    def initAll(self):
        # 初始化matrix里所有为1的点
        for i in range(self.N):
            for j in range(self.M):
                if self.grid[i][j] == 1:
                    dot = Dot()
                    self.dots[i][j] = dot
                    self.fatherMap[dot] = dot
                    self.sizeMap[dot] = 1
                    if i == 0:
                        self.cellingSet.add(dot)
                        self.cellingAll += 1
        # 初始化matrix里所有为1的点的连接
        for i in range(self.N):
            for j in range(self.M):
                self.union(i, j, i - 1, j)
                self.union(i, j, i + 1, j)
                self.union(i, j, i, j - 1)
                self.union(i, j, i, j + 1)

    def isValid(self, r, c):
        return r >= 0 and r < self.N and c >= 0 and c < self.M and self.grid[r][c] == 1

    def findFather(self, dot):
        if self.fatherMap[dot] == dot:
            return dot

        father = self.findFather(self.fatherMap[dot])
        self.fatherMap[dot] = father
        return father

    def union(self, r1, c1, r2, c2):
        if not self.isValid(r1, c1) or not self.isValid(r2, c2):
            return
        dot1 = self.dots[r1][c1]
        dot2 = self.dots[r2][c2]

        father1 = self.findFather(dot1)
        father2 = self.findFather(dot2)
        if (father1 == father2):
            return

        size1 = self.sizeMap[father1]
        size2 = self.sizeMap[father2]

        big = father1 if size1 > size2 else father2
        small = father2 if big == father1 else father1
        bigSize = max(size1, size2)
        smallSize = min(size1, size2)
        self.fatherMap[small] = big
        self.sizeMap[big] = size1 + size2

        status1 = big in self.cellingSet
        status2 = small in self.cellingSet
        if status1 ^ status2:
            self.cellingSet.add(big)
            self.cellingAll += bigSize if status2 else smallSize

    def calculateResult(self, i, j):
        preCellingAll = self.cellingAll

        dot = Dot()
        self.grid[i][j] = 1
        self.dots[i][j] = dot
        self.fatherMap[dot] = dot
        self.sizeMap[dot] = 1
        if i == 0:
            self.cellingSet.add(dot)
            self.cellingAll += 1
        self.union(i, j, i - 1, j)
        self.union(i, j, i + 1, j)
        self.union(i, j, i, j - 1)
        self.union(i, j, i, j + 1)

        return 0 if preCellingAll == self.cellingAll else self.cellingAll - preCellingAll - 1


# 给定一个矩阵，第0行代表天花板， metrix[i][j] == 1 代表在 i行j列有炸弹，炸弹和天花板有粘性可以黏住上下左右4个方向的炸弹
# 给定第二个矩阵，shot[i] 长度固定为2，分别代表射击metrix上的r坐标c坐标，每次击爆一个炸弹以后，和天花板断开联系的炸弹就会掉地上
# 求一个数组，代表每次射击击落的炸弹数量
class Solution:

    def bomb(self, metrix, shot):
        self.N = len(metrix)
        self.M = len(metrix[0])
        self.grid = metrix
        for i in range(len(shot)):
            if self.isValid(shot[i][0], shot[i][1]):
                self.grid[shot[i][0]][shot[i][1]] = 2

        unionFind = UnionFind(self.grid)
        # 从后向前计算，合并新的结果减去旧的就是这次射击击落的个数
        res = [0 for _ in range(len(shot))]
        for i in range(len(shot) - 1, -1, -1):
            if self.grid[shot[i][0]][shot[i][1]] == 2:
                res[i] = unionFind.calculateResult(shot[i][0], shot[i][1])

        return res

    def isValid(self, r, c):
        return r >= 0 and r < self.N and c >= 0 and c < self.M and self.grid[r][c] == 1


so = Solution()
M = [[1, 0, 0, 1, 0], [1, 0, 0, 1, 1], [1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 1, 1, 0]]
shot = [[2, 0], [1, 3], [1, 4], [0, 3]]
print(so.bomb(M, shot))






