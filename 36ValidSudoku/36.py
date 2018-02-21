class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(0, 9):
            rowSet = set()
            colSet = set()
            cellSet = set()
            for j in range(0, 9):
                if board[i][j] != '.' and board[i][j] in rowSet:
                    return False
                rowSet.add(board[i][j])
                if board[j][i] != '.' and board[j][i] in colSet:
                    return False
                colSet.add(board[j][i])
                rowIndex = 3 * (i // 3)
                colIndex = 3 * (i % 3)
                if board[rowIndex + j // 3][colIndex + j % 3] != '.' \
                    and board[rowIndex + j // 3][colIndex + j % 3] in cellSet:
                    return False
                cellSet.add(board[rowIndex + j // 3][colIndex + j % 3])
        return True