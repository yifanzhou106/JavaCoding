class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        count = 0
        numbers = []
        result = 0
        possitive = True
        isSignUsed = False

        for c in str:
            if c == ' ' and count == 0:
                continue
            elif c == '+' and count == 0:
                possitive = True
                isSignUsed = True
                count += 1
            elif c == '-' and count == 0:
                possitive = False
                isSignUsed = True
                count += 1
            elif ord(c) >= ord('0') and ord(c) <= ord('9'):
                count += 1
                numbers.append(ord(c) - ord('0'))
            elif count != 0 and (ord(c) < ord('0') or ord(c) > ord('9')):
                break
            else:
                break

        if count is not 0:
            if isSignUsed == True:
                count = count - 1
            result = self.buildNumber(numbers, count, possitive)

        return result

    def buildNumber(self, numbers, count, possitive):
        result = 0
        for num in numbers:
            result += num * 10 ** (count - 1)
            count -= 1
        if result >= 1 << 31:
            if possitive is False:
                result = 1 << 31
            else:
                result = (1 << 31) - 1
        if possitive is False:
            result = -result

        return result