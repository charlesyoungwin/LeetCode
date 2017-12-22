from collections import deque

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        click = tuple(click)
        R, C = len(board), len(board[0])

        def neighbors(r, c):
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if (dr or dc) and 0 <= r + dr < R and 0 <= c + dc < C:
                        yield r + dr, c + dc

        queue = deque([click])
        seen = {click}
        while queue:
            r, c = queue.popleft()
            if board[r][c] == 'M':
                board[r][c] = 'X'
            else:
                mines_adj = sum( board[nr][nc] in 'MX' for nr, nc in neighbors(r, c))
                if mines_adj:
                    board[r][c] = str(mines_adj)
                else:
                    board[r][c] = 'B'
                    for nei in neighbors(r, c):
                        if board[nei[0]][nei[1]] == 'E' and nei not in seen:
                            queue.append(nei)
                            seen.add(nei)
        return board

if __name__ == '__main__':
    solu = Solution()
    board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
    click = [3, 0]
    for item in solu.updateBoard(board, click):
        print(item)