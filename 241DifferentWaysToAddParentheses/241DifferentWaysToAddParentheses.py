class Solution:

    # not ac, wrong answer
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        import re

        # p = re.compile(r'([\+\-\*]?)(\d+)')
        # length = len(p.findall(input))
        #
        # A = [0] * (length + 1)
        # A[0] = 1
        # A[1] = 1
        # A[2] = 1
        # for i in range(3, length + 1):
        #     for j in range(1, i):
        #         A[i] += A[j] * A[i - j]
        # return A[length]

        p = re.compile(r'([\+\-\*]?)(\d+)')
        res = p.findall(input)
        A = [[0 for _ in range(len(res))] for _ in range(len(res))]
        for i in range(len(res)):
            A[i][i] = int(res[i][0] + res[i][1]) if i == 0 else int(res[i][1])
        for i in range(len(res) - 1):
            if res[i + 1][0] == '+':
                A[i][i + 1] = A[i][i] + A[i + 1][i + 1]
            if res[i+1][0] == '-':
                A[i][i+1] = A[i][i] - A[i+1][i+1]
            if res[i + 1][0] == '*':
                A[i][i + 1] = A[i][i] * A[i + 1][i + 1]
        result = []
        def compute(start, end):
            if start > end:
                return 0
            if start == end:
                return A[start][end]
            if start == end - 1:
                return A[start][end]
            ######################
            #这里的逻辑有问题，循环一次就结束了。。。暂时找不到解决的办法。
            for i in range(start, end):
                k = compute(start, i) + compute(i + 1, end)
                result.append(k)
                return k


        ans = compute(0, len(res) - 1)
        return result, ans

    def diffWaysToComputeV2(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToComputeV2(input[:i])
                res2 = self.diffWaysToComputeV2(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res

    def helper(self, m, n, op):
        if op == '+':
            return m + n
        elif op == '-':
            return m - n
        else:
            return m * n

if __name__ == '__main__':
    input = "2-1-1-1"
    print(Solution().diffWaysToComputeV2(input))


