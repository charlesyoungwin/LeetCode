class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = [0 for i in range(len(matrix[0]))]
        area = 0
        for layer in matrix:
            for i in range(len(layer)):
                if layer[i] == '1':
                    res[i] += 1
                else:
                    res[i] = 0
            area = max(area, self.histogram(res))
        return area

    def histogram(self, hist):
        stack = [-1]
        hist.append(0)
        res = 0
        for i in range(len(hist)):
            
            while hist[i] < hist[stack[-1]]:
                index = stack.pop()
                h = hist[index]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        hist.pop()
        return res

if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
              ["1","1","1","1","1"],["1","0","0","1","0"]]
    print(Solution().maximalRectangle(matrix))


