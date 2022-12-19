class Solution:
    def prefectShuffle(self, s):
        string = list(s)
        self.process(string, 0, len(s) - 1)
        return ''.join(string)

    def process(self, s, left, right):
        if left > right:
            return
        k = 1
        base = 3
        length = right - left + 1
        while (base * 3 - 1) < length:
            base *= 3
            k += 1
        mid = left + ((right - left) >> 1)
        leftNumCount = base - 1
        self.swapString(s, left + leftNumCount // 2, mid + leftNumCount // 2, mid)
        self.replace(s, left, left + leftNumCount - 1, k)
        self.process(s, left + leftNumCount, right)

    def swapString(self, s, left, right, mid):
        l = left
        m = mid
        while l < m:
            s[l], s[m] = s[m], s[l]
            l += 1
            m -= 1
        m = mid + 1
        r = right
        while m < r:
            s[m], s[r] = s[r], s[m]
            m += 1
            r -= 1
        l = left
        r = right
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    # 1234 5678 = > 转换公式
    def nextIndex(self, i, N):
        if i > N:
            return ((i - N) * 2) - 1
        else:
            return i * 2

# 要注意公式对应的是1,3,9,27开始，要减1
    def replace(self, s, left, right, k):
        trigger = 1
        length = (right - left + 1) // 2
        for i in range(k):
            pre = s[trigger + left - 1]
            cur = self.nextIndex(trigger, length)
            while cur != trigger:
                tmp = s[cur + left - 1]
                s[cur + left - 1] = pre
                pre = tmp
                cur = self.nextIndex(cur, length)
            s[cur + left - 1] = pre
            trigger *= 3


so = Solution()
s = '12345678'
print(so.prefectShuffle(s))
