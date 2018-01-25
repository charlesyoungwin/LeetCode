class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {}
        dic['2'] = 'abc'
        dic['3'] = 'def'
        dic['4'] = 'ghi'
        dic['5'] = 'jkl'
        dic['6'] = 'mno'
        dic['7'] = 'pqrs'
        dic['8'] = 'tuv'
        dic['9'] = 'wxyz'
        dic['0'] = ''
        dic['1'] = ''
        res = []
        self.backtrack(dic, digits, res, "", 0)
        return res

    def backtrack(self, dic, digits, res, path, start):
        if path and len(path) == len(digits) :
            res.append(path)
            
        for i in range(start, len(digits)):
            for item in dic[digits[i]]:
                self.backtrack(dic, digits, res, path + item, i + 1)


if __name__ == '__main__':
    digits = "233"
    print(Solution().letterCombinations(digits))