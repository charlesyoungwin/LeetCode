class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])
        res = []
        row, col, d = 0, 0, 1
        for i in range(m * n):
            res.append(matrix[row][col])
            row -= d
            col += d
            if row >= m:
                row = m - 1
                col += 2
                d = -d
            if col >= n:
                col = n - 1
                row += 2
                d = -d
            if row < 0:
                row = 0
                d = -d
            if col < 0:
                col = 0
                d = -d
        return res

    def findDiagonalOrder2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])
        row, col = 0, 0
        res = []
        for i in range(m * n):
            res.append(matrix[row][col])
            if (row + col) % 2 == 0: #向上

                if col == (n - 1):
                    row = row + 1
                elif row == 0:
                    col = col + 1
                else:
                    row = row - 1
                    col = col + 1
            else:   #向下
                if row == (m - 1):
                    col = col + 1
                elif col == 0:
                    row = row + 1
                else:
                    row = row + 1
                    col = col - 1
        return res

    def findDiagonalOrder3(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        entries = [(i + j, (j, i)[(i ^ j) & 1], val)
                   for i, row in enumerate(matrix)
                   for j, val in enumerate(row)]
        return [e[2] for e in sorted(entries)]

if __name__ == '__main__':
    solu = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("solution1:")
    print(solu.findDiagonalOrder(matrix))
    print("solution2:")
    print(solu.findDiagonalOrder2(matrix))
    print("solution3:")
    print(solu.findDiagonalOrder3(matrix))