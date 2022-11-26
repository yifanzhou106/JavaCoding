class Manacher:
    def findLongestPalindromeString(self, strList):
        str = ''.join(strList)
        redius = [0 for _ in range(len(str))]
        r = -1
        c = 0
        i = 0
        while r < (len(str) - 1):

            if r < i:
                count = 1
                while (i - count) >= 0 and (i + count) < len(str) and str[(i - count)] == str[i + count]:
                    redius[i] += 1
                    r = i + count
                    c = i
                    count += 1

            else:
                left = self.findLeft(c, i)

                if (left - redius[left]) > self.findLeft(c, r):
                    redius[i] = redius[left]
                elif ((left - redius[left]) < self.findLeft(c, r)):
                    redius[i] = r - i
                else:
                    count = r - i + 1
                    redius[i] = r - i
                    while (i - count) >= 0 and (i + count) < len(str) and str[(i - count)] == str[i + count]:
                        redius[i] += 1
                        r = i + count
                        c = i
                        count += 1

            i += 1
        print(redius)
        print(c, r)

        i = c - redius[c] - 1
        while i >= 0:
            strList.append(strList[i])
            i -= 1
        res = []
        for c in strList:
            if c != '#':
                res.append(c)

        return ''.join(res)

    def findSolution(self, str):
        temp = ['#']
        for c in str:
            temp.append(c)
            temp.append('#')
        print(''.join(temp))
        return self.findLongestPalindromeString(temp)

    def findLeft(self, c, i):
        return c - (i - c)


so = Manacher()
str = 'abc1232'
print(so.findSolution(str))