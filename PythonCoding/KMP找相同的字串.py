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
