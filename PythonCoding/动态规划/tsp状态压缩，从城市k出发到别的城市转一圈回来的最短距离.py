# 状态压缩优化问题
# 有N个城市，任意一个城市到自己的距离为0，点到点的距离记录在metrix M里，
# 要求一个人从k城市出发，必须经过每一个城市且只能在一座城市停留一次，最后返回初始点，
# 求返回的最短距离
class Solution:
    # 解法1 递归暴力
    def tsp_problem1(self, M):
        N = len(M)
        isVisited = [False for _ in range(N)]
        return self.process(M, N, isVisited, 0)
    # 当前节点挑选一个下次的目的地
    # 当前节点到下次的目的地 + 下次的目的地中距离最小值
    def process(self, M, N, isVisited, cur):
        rest = 0
        for i in range(N):
            if not isVisited:
                rest += 1
        # 当只有一个城市的时候，就是返回从当前城市到初始城市的距离
        if rest == 1:
            return M[cur][0]

        isVisited[cur] = True
        res = float('inf')
        for i in range(N):
            if not isVisited[i] and i != cur:
                res = min(res, M[cur][i] + self.process(M, N, isVisited, i))

        isVisited[cur] = False
        return res

    # 解法2 状态压缩
    def tsp_problem2(self, M):
        N = len(M)
        cityStatus= (1 << N) - 1
        return self.process2(M, N, cityStatus, 0)
    def process2(self, M, N, cityStatus, cur):

        if cityStatus == cityStatus & (~cityStatus +1):
            return M[cur][0]

        city &= ~(1 << cur)
        res = float('inf')
        for move in range(N):
            if (cityStatus & (1<<move) != 0) and move != cur:
                res = min(res, M[cur][move] + self.process(M, N, cityStatus, move))

        city |= 1 << cur
        return res

