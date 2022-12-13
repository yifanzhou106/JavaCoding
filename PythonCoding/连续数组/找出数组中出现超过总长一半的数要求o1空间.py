
class Solution:

    def printNumIfCountMoreThanNDK(self, arr, k):
        map = {}

        for i in range(len(arr)):
            if len(map) < k:
                map[arr[i]] = 1
            elif arr[i] in map:
                map[arr[i]] += 1
            else:
                for key in list(map):
                    map[key] -= 1
                    if map[key] == 0:
                        del map[key]
        res = []
        for key in map:
            count = 0
            for i in range(len(arr)):
                if arr[i] == key:
                    count += 1
            if count > len(arr) // k:
                res.append(key)
        return res
so = Solution()

arr = [1 ,1 ,1 ,2 ,2 ,2 ,2 ,3 ,3 ,3 ,3 ,4 ,4 ,4 ,4]
print(so.printNumIfCountMoreThanNDK(arr ,4))