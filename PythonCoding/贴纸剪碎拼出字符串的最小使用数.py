class Solution:
    def minStickers(self, target, arr):
        map = [[0 for _ in range(26)] for _ in range(len(arr))]
        for i in range(len(arr)):
            for c in arr[i]:
                map[i][self.cToNum(c)] += 1
        dp = {}
        dp[""] = 0
        return self.process(target, map, dp)

    def process(self, rest, map, dp):
        if rest in dp:
            return dp[rest]

        rMap = [0 for _ in range(26)]
        for c in rest:
            rMap[self.cToNum(c)] += 1

        ans = float('inf')
        for i in range(len(map)):
            sb = []
            # 剩下字符中必须要有一个可以被目前sticker处理，不然没办法缩短rest导致栈溢出
            if map[i][self.cToNum(rest[0])] == 0:
                continue
            for j in range(26):
                if rMap[j] > 0:
                    for _ in range(max(0, rMap[j] - map[i][j])):
                        sb.append(chr(j + ord('a')))
            s = "".join(sb)
            tmp = self.process(s, map, dp)
            if tmp != -1:
                ans = min(ans, tmp + 1)
        dp[rest] = -1 if ans == float('inf') else ans
        return dp[rest]

    def cToNum(self, c):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            return ord(c) - ord('a')
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            return ord(c) - ord('A')


so = Solution()
arr = ["aaaa", "bbaa", "ccddd"]
str = "abcccccdddddbbbaaaaa"
print(so.minStickers(str, arr))
