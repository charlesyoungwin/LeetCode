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
        print(res)
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

    #solutionV2
    def existV2(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(startX, startY, index):
            if index == len(word):
                return True
            if startX < 0 or startY < 0 or startX >= len(board) or startY >= len(board[0]) or word[index] != board[startX][startY]:
                return False
            tmp = board[startX][startY]
            board[startX][startY] = '#'
            res =   dfs(startX + 1, startY, index + 1) or \
                    dfs(startX - 1, startY, index + 1) or \
                    dfs(startX, startY + 1, index + 1) or \
                    dfs(startX, startY - 1, index + 1)
            board[startX][startY] = tmp
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
    print(Solution().existV2(board, word))