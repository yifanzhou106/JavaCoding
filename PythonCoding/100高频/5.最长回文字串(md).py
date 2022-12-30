class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        newS = ['#']
        for c in s:
            newS.append(c)
            newS.append('#')

        d = self.manacher(newS)
        print(d)
        maxIndex = 0
        maxD = 0
        for i in range(len(d)):
            if d[i] > maxD:
                maxD = d[i]
                maxIndex = i
        # 半径是((maxD * 2 + 1) >> 1)
        startIndex = maxIndex - ((maxD * 2 + 1) >> 1)
        endIndex = maxIndex + ((maxD * 2 + 1) >> 1)

        res = ["" for _ in range(maxD)]
        j = 0
        for i in range(startIndex, endIndex + 1):
            if newS[i] != '#':
                res[j] = newS[i]
                j += 1
        return ''.join(res)

    def manacher(self, s):
        N = len(s)
        d = [0 for _ in range(N)]
        c = 0
        r = -1

        for i in range(N):
            if i > r:
                count = 1
                r = i
                c = i
                while i + count < N and i - count >= 0 and s[i + count] == s[i - count]:
                    r += 1
                    count += 1
                    d[i] += 1

            leftI = self.findLeft(c, i)
            leftR = self.findLeft(c, r)

            if leftI - d[leftI] > leftR:
                d[i] = d[leftI]
            elif leftI - d[leftI] < leftR:
                d[i] = r - i
            else:
                count = r - i + 1
                d[i] = r - i
                c = i
                while i + count < N and i - count >= 0 and s[i + count] == s[i - count]:
                    r += 1
                    count += 1
                    d[i] += 1
        return d

    def findLeft(self, c, i):
        return c - (i - c)

