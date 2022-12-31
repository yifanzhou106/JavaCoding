# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串""。
# 示例 1：
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。

# 直接用第一个string和其他的比较
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        length = float('inf')
        first = strs[0]
        for s in strs:
            i = 0
            while i < min(len(s),len(first)) and s[i] == first[i]:
                i += 1
            length = min(length, i)
        return first[:length]



