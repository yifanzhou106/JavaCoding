class Solution:

    def f(self, N):
        if N < 5:
            return "s" if N == 0 or N == 2 else "f"
        temp = 1
        while temp <= N:
            tmp = self.f(N - temp)
            if self.f(N - temp) == "s":
                return "f"
            if temp > (N >> 2):
                break
            temp = temp << 2
        return "s"


so = Solution()
for i in range(50):
    print(i, so.f(i))
