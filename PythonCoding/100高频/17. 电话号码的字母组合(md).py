class Solution(object):
    # 通过不停循环更新res数组
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map = [['','',''], ['','',''], ['a','b','c'], ['d','e','f'], ['g','h','i'],['j','k','l'], ['m','n','o'], ['p','q','r','s'],['t','u','v'], ['w','x','y','z']]
        res = []

        for d in digits:
            d = ord(d)-ord('0')
            if not res:
                res = map[d][:]
            else:
                tmp = []
                for r in res:
                    for c in map[d]:
                        tmp.append(r+c)
                res = tmp
        return res
