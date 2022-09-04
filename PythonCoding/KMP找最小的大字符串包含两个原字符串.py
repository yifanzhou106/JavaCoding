# Online Python compiler (interpreter) to run Python o
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

    def findSmallestStringContainsTwoOriginStr(self, str):
        temp = str + 'k'
        self.findNext(temp)
        res = []
        for i in range(self.next[-1], len(str)):
            str += str[i]
        return str


kmp = KMP()
str2 = 'abaca'
print(kmp.findSmallestStringContainsTwoOriginStr(str2))