class Solution:
    # 环上有字母，我们要通过旋转环到12点钟方向才可以按下输入字母
    # 环可以逆时针顺时针转动，每转动一次记一步，按下确认键记一步， 求最少步数

    def enterKey(self, ring, key):
        map = {}
        rsize = len(ring)
        for i in range(rsize):
            indexs = map.get(ring[i], [])
            indexs.append(i)
            map[ring[i]] = indexs
        return self.process(ring, key, map, rsize, 0, 0)

    # 用dfs来解， 每次从ri开始，尝试所有下一个key字母的位置，得到最小值
    def process(self, ring, key, map, rsize, ri, ki):
        if ki == len(key):
            return 0
        indexs = map[key[ki]]
        res = float('inf')
        for index in indexs:
            tmp = self.findShortestPathInRing(ri, index, rsize) + 1 + self.process(ring, key, map, rsize, index, ki + 1)
            res = min(res, tmp)
        return res

    # 求出从f到t的最小步数
    def findShortestPathInRing(self, f, t, rsize):
        # 分别是右半圈和左半圈
        return min(abs(f - t), min(f, t) + rsize - max(f, t))


so = Solution()
r = 'godding'
k = 'gd'
print(so.enterKey(r, k))

# 记忆化搜索
class Solution:
    # 环上有字母，我们要通过旋转环到12点钟方向才可以按下输入字母
    # 环可以逆时针顺时针转动，每转动一次记一步，按下确认键记一步， 求最少步数

    def enterKey(self, ring, key):
        map = {}
        rsize = len(ring)
        for i in range(rsize):
            indexs = map.get(ring[i], [])
            indexs.append(i)
            map[ring[i]] = indexs
        dp = [[None for _ in range(len(key) + 1)] for _ in range(len(ring))]
        return self.process(ring, key, map, rsize, 0, 0, dp)

    # 用dfs来解， 每次从ri开始，尝试所有下一个key字母的位置，得到最小值
    def process(self, ring, key, map, rsize, ri, ki, dp):
        if dp[ri][ki]:
            return dp[ri][ki]
        if ki == len(key):
            dp[ri][ki] = 0
            return dp[ri][ki]
        indexs = map[key[ki]]
        res = float('inf')
        for index in indexs:
            tmp = self.findShortestPathInRing(ri, index, rsize) + 1 + self.process(ring, key, map, rsize, index, ki + 1,
                                                                                   dp)
            res = min(res, tmp)
        dp[ri][ki] = res
        return dp[ri][ki]

    # 求出从f到t的最小步数
    def findShortestPathInRing(self, f, t, rsize):
        # 分别是右半圈和左半圈
        return min(abs(f - t), min(f, t) + rsize - max(f, t))


so = Solution()
r = 'godding'
k = 'gd'
print(so.enterKey(r, k))