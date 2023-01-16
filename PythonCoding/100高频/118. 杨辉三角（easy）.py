class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        pre = self.generate(numRows - 1)
        lastRow = pre[-1]
        tmp = [1 for _ in range(len(lastRow) + 1)]
        for i in range(1, len(tmp) - 1):
            tmp[i] = lastRow[i - 1] + lastRow[i]
        pre.append(tmp[:])
        return pre




