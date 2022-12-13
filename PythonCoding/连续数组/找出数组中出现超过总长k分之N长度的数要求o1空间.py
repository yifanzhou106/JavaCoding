
class Solution:
    def printNumIfCountMoreThanHalf(self, arr):
        cand = 0
        hp = 0
        for i in range(len(arr)):
            if hp == 0:
                cand = arr[i]
                hp = 1
            elif arr[i] == cand:
                hp += 1
            else:
                hp -= 1
        count = 0
        for i in range(len(arr)):
            if arr[i] == cand:
                count += 1
        return cand if count > len(arr) // 2 else None

so = Solution()

arr = [1 ,1 ,1 ,2 ,6 ,66 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,6 ,2 ,2]
print(so.printNumIfCountMoreThanHalf(arr))
