class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(int(j), int(k), input[i]))
        return res

    def helper(self, j, k, op):
        if op == '+':
            return j + k
        elif op == '-':
            return j - k
        else:
            return j * k

if __name__ == '__main__':
    input = "2*3-4*5"
    print(Solution().diffWaysToCompute(input))