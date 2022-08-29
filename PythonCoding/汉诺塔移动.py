class Solution:
    def hanoi(self, n):
        self.rec(n, "Left", "Right", "Middle")

    def rec(self, n, From, To, Temp):
        if n == 1:
            print("move " + str(n) + " from " + From + " to " + To)
        else:
            self.rec(n - 1, From, Temp, To)
            print("move " + str(n) + " from " + From + " to " + To)
            self.rec(n - 1, Temp, To, From)


so = Solution()

so.hanoi(3)
