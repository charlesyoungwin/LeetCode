class Solution:

    # bottom-top solution
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtracking(res, s,  open, close, maxNum):
            if len(s) == maxNum * 2:
                res.append(s)
                return
            if open < maxNum:
                backtracking(res, s + "(" , open + 1, close, maxNum)
            if close < open:
                backtracking(res, s + ")", open, close + 1, maxNum)
        res = []
        backtracking(res, "", 0, 0, n)
        return res

    #top-bottom solution
    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(s, left, right):
            if left > right:
                return
            if not left and not right:
                res.append(s)
            if left > 0:
                dfs(s + "(", left - 1, right)
            if right > 0:
                dfs(s + ")", left, right - 1)
        dfs("", n, n)
        return res

    #生成器
    def generateParenthesis3(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left - 1, right) : yield q
                for q in generate(p + ')', left, right - 1) : yield q
        return list(generate('', n, n))




if __name__ == '__main__':
    solu = Solution()
    for item in solu.generateParenthesis3(3):
        print(item)