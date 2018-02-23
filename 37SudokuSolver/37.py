class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.isSolve(board)

    def isSolve(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    for value in [str(i) for i in range(1, 10)]:
                        if self.isValid(board, i, j, value):
                            board[i][j] = value
                            if self.isSolve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
        
    def isValid(self, board, row, col, c):
        for i in range(0, 9):
            if board[i][col] != '.' and board[i][col] == c:
                return False
            if board[row][i] != '.' and board[row][i] == c:
                return False
            value = board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3]
            if value != '.' and value == c:
                return False
        return True

if __name__ == '__main__':
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    Solution().solveSudoku(board)
    print(board)