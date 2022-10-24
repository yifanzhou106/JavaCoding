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


so = Solution()

arr = [70, 100, 3, 1]
print(so.winner(arr))