class Solution:
    def winner(self, cards):
        if not cards:
            return 0
        return max(self.f(cards, 0, len(cards) - 1), self.s(cards, 0, len(cards) - 1))

    def f(self, cards, l, r):
        if l == r:
            return cards[l]
        p1 = cards[l] + self.s(cards, l + 1, r)
        p2 = cards[r] + self.s(cards, l, r - 1)

        return max(p1, p2)

    def s(self, cards, l, r):
        if l == r:
            return 0
        return min(self.f(cards, l + 1, r), self.f(cards, l, r - 1))

    def winnerDP(self, cards):
        f = [[0 for _ in range(len(cards))] for _ in range(len(cards))]
        s = [[0 for _ in range(len(cards))] for _ in range(len(cards))]
        for i in range(len(cards)):
            f[i][i] = cards[i]
            s[i][i] = 0

        for k in range(1, len(cards)):
            i = 0
            j = k
            while i < len(cards) and j < len(cards):
                f[i][j] = max(cards[i] + s[i + 1][j], cards[j] + s[i][j - 1])
                s[i][j] = min(f[i + 1][j], f[i][j - 1])
                i += 1
                j += 1

        return max(f[0][len(cards) - 1], s[0][len(cards) - 1])


so = Solution()

arr = [70, 100, 3, 1]
print(so.winner(arr))
print(so.winnerDP(arr))