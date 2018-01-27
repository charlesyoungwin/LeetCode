class Solution:

    #time exceeded
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        res = []
        self.dfs(board, word, [], 0, res)
        return True if res else False

    def dfs(self, board, word, path, index, res):
        if index == len(word):
            if len(path) == len(word):
                res.append(path)
        for i in range(index, len(word)):
            for point in self.position(board, word[i]):
                if not path or (self.isNeighbor(point, path[-1]) and point not in path):
                    self.dfs(board, word, path + [point], i + 1, res)

    def position(self, board, character):
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == character:
                    res.append([i, j])
        return res

    def isNeighbor(self, pointA, pointB):
        if abs(pointA[0] - pointB[0]) == 1 and pointA[1] - pointB[1] == 0:
            return True
        elif abs(pointA[1] - pointB[1]) == 1 and pointA[0] - pointB[0] == 0:
            return True 
        else:
            return False


    #solution2
    def existV2(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            tmp = board[i][j]
            board[i][j] = '#'
            res = dfs(i + 1, j, index + 1) or dfs(i - 1, j, index + 1) or dfs(i, j - 1, index + 1)\
                    or dfs(i, j + 1, index + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0) == True:
                    return True
        return False

if __name__ == '__main__':
    board = [
              ['A','B','C','E'],
              ['E','F','C','S'],
              ['A','D','E','E']
            ]
    # board = [
    #             ['a', 'b'],
    #             ['c', 'd']
    #         ]

    word = "ABCCE"

    print("solution1")
    print(Solution().exist(board, word))
    print("solution2")
    print(Solution().existV2(board, word))