# 用head 和tail 两个map，存头尾，删除中间的
# 
class Solution:
    def longestSequenceCount(self, arr):
        head = {}
        tail = {}
        maxCount = 0
        for i in range(len(arr)):
            head[arr[i]] = 1
            tail[arr[i]] = 1

            if arr[i] - 1 in tail:
                preCount = tail[arr[i] - 1]
                headIndex = arr[i] - preCount
                head[headIndex] = preCount + 1
                tail[arr[i]] = preCount + 1
                maxCount = max(maxCount, preCount + 1)
                del head[arr[i]]
                del tail[arr[i] - 1]

            # 需要多更新最头结点和最尾结点
            if arr[i] + 1 in head:
                preCount = head[arr[i] + 1]
                tailIndex = arr[i] + preCount
                headIndex = arr[i] - tail[arr[i]] + 1
                tail[tailIndex] = preCount + tail[arr[i]]
                head[headIndex] = preCount + tail[arr[i]]
                maxCount = max(maxCount, preCount + tail[arr[i]])
                del head[arr[i] + 1]
                del tail[arr[i]]
            print(head, tail)
        return maxCount


so = Solution()
arr = [0, 100, 4, 200, 1, 3, 2]
print(so.longestSequenceCount(arr))
