class Solution:
    def mostPointCrossLine(self, X, Y):
        res = 0
        for i in range(len(X)):
            allSame = 1
            sameX = 0
            sameY = 0
            sameScope = 0
            map = {}
            for j in range(i + 1, len(X)):
                if X[j] == X[i] and Y[j] == Y[i]:
                    allSame += 1
                elif X[j] == X[i]:
                    sameX += 1
                elif Y[j] == Y[i]:
                    sameY += 1
                else:
                    x = X[i] - X[j]
                    y = Y[i] - Y[j]
                    d = self.gcd(x, y)
                    scope = ""
                    if x < 0 or y < 0:
                        scope = "-"
                    scope += str(abs(y) // d) + '_' + str(abs(x) // d)
                    map[scope] = map.get(scope, 0) + 1
                    sameScope = max(sameScope, map[scope])
            res = max(res, allSame + max(sameX, sameY, sameScope))
        return res

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)


so = Solution()
x = [1, 4, 5, 3, 9]
y = [4, 4, 3, 6, 12]
print(so.mostPointCrossLine(x, y))
