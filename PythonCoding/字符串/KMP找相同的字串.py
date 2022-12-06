class KMP:

    def findNext(self, str):
        self.next = [None for _ in range(len(str))]
        self.next[0] = -1
        if len(str) == 1:
            return [-1]
        for i in range(1, len(str)):
            self.next[i] = self.rec(i, i, str)

    def rec(self, i, j, str):
        if self.next[i] == -1 or self.next[i - 1] == -1:
            return 0
        elif str[self.next[i - 1]] == str[j - 1]:
            return self.next[i - 1] + 1
        else:
            return self.rec(self.next[i - 1], j, str)

    def findSameSubString(self, str1, str2):
        i = 0
        j = 0
        self.findNext(str2)
        print(next)

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            elif self.next[j] == -1:
                i += 1
            else:
                j = self.next[j]
        return True if j == len(str2) else False


kmp = KMP()
str1 = 'ababcababtk'
str2 = 'caba'
print(kmp.findSameSubString(str1, str2))


class Solution2:
    def KMP(self, s1, s2):
        if len(s2) == 0 or len(s1) == 0 or len(s2) > len(s1):
            return -1

        next = self.findNext(s2)

        j = 0
        i = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            elif j == -1:
                i += 1
                j = 0
            else:
                j = next[j]
        return i - j if j == len(s2) else -1

    def findNext(self, s):
        next = [0 for _ in range(len(s))]
        next[0] = -1

        for i in range(2, len(s)):
            cur = i - 1
            while cur != -1 and s[i - 1] != s[next[cur]]:
                cur = next[cur]
            next[i] = 0 if cur == -1 else next[cur] + 1
        return next


so = Solution2()
s1 = "aabaacaabaak"
s2 = "aabaak"
print(so.KMP(s1, s2))

