
class Solution:
    def shortestPathConvert(self ,start ,to ,arr):
        arr.append(start)
        nears = self.findNears(arr)
        distances = self.findDistances(nears, start)
        paths = []
        self.dfs(start ,to ,nears ,distances ,distances[to] ,paths ,[start])

        return paths

    def dfs(self, cur, to, nears, distances ,shortest, paths, path ):

        if distances[cur] == shortest and cur == to:
            paths.append(path[:])
            return
        near = nears[cur]
        for nextStr in near:
            if distances[nextStr] == distances[cur] + 1:
                path.append(nextStr)
                self.dfs(nextStr ,to ,nears ,distances ,shortest ,paths ,path)
                path.pop()


    def findNears(self, arr):
        strs = set()
        for s in arr:
            strs.add(s)
        nearMap = {}
        for s in strs:
            nearMap[s] = self.findNear(s ,strs)

        return nearMap

    def findNear(self, s, strs):
        res = []
        listStr = list(s)
        for i in range(len(s)):
            for j in range(26):
                c = chr(ord('a') + j)
                if listStr[i] == c:
                    continue
                tmp = listStr[i]
                listStr[i] = c
                if ''.join(listStr) in strs:
                    res.append(''.join(listStr))
                listStr[i] = tmp
        return res

    def findDistances(self, nears, start):
        visited = set()
        distances = {}
        q = [start]
        distances[start] = 0
        visited.add(start)
        while q:
            s = q.pop(0)
            near = nears[s]
            for nextStr in near:
                if nextStr in visited:
                    continue
                distances[nextStr] = distances[s] + 1
                visited.add(nextStr)
                q.append(nextStr)
        return distances

so = Solution()
start = 'abc'
to = 'cab'
arr = ['cab' ,'acc', 'cbc', 'ccc', 'cac', 'cbb', 'aab', 'abb']
print(so.shortestPathConvert(start ,to ,arr))

