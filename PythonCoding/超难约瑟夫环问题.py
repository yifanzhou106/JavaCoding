# 两个公式
# 号 = (数 - 1)%i + 1
# 旧 = (新 + s -1) % i + 1
# ==> s = (m - 1) % i +1
# 旧 = (新 + (m - 1) % i +1 -1) % i + 1 ==> 旧 = (新 + m - 1) % i + 1
class Solution:
    def josephusKill(self, head, m):
        count = 1
        cur = head.next
        while cur != head:
            count += 1
            cur = cur.next

        n = self.getLive(count, m)
        for _ in range(n - 1):
            head = head.next
        head.next = head
        return head

    def getLive(self, i, m):
        if i == 1:
            return 1

        return (self.getLive(i - 1, m) + m - 1) % i + 1
